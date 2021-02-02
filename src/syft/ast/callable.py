# stdlib
from types import ModuleType
from typing import Any
from typing import Callable as CallableT
from typing import List
from typing import Optional
from typing import Tuple
from typing import Union

# syft relative
from .. import ast
from .. import lib
from ..core.node.abstract.node import AbstractNodeClient
from ..core.node.common.action.function_or_constructor_action import (
    RunFunctionOrConstructorAction,
)
from ..logger import traceback_and_raise
from .util import module_type


class Callable(ast.attribute.Attribute):
    def __init__(
        self,
        path_and_name: str,
        object_ref: Optional[Any] = None,
        return_type_name: Optional[str] = None,
        require_pargs: bool = False,
        parg_list: List[Any] = [],
        client: Optional[AbstractNodeClient] = None,
        is_static: Optional[bool] = False,
    ):
        """
        A Callable represent a method (can be static), global function, or constructor which can be
        directly executed.


         Args:
             client (Optional[AbstractNodeClient]): The client for which all computation is being executed.
             path_and_name (str): The path for the current node. Eg. `syft.lib.python.List`
             object_ref (Any): The actual python object for which the computation is being made.
             return_type_name (Optional[str]): The return type name of the given action as a
                 string (the full path to it, similar to path_and_name).
             is_static (bool): if True, the object has to be solved on the AST, not on an
                existing pointer.
        """

        super().__init__(
            path_and_name=path_and_name,
            object_ref=object_ref,
            return_type_name=return_type_name,
            require_pargs=require_pargs,
            parg_list=parg_list,
            client=client,
        )

        self.is_static = is_static

    def __call__(
        self,
        *args: Tuple[Any, ...],
        **kwargs: Any,
    ) -> Optional[Union["Callable", CallableT]]:
        """
        The __call__ method on a Callable has two possible roles:

        1. If the client is set, execute the function for it and return the appropriate pointer
        given the return type name.

        2. If the client is not set, then is being used as a query on the ast.
        """
        if self.client is not None:
            return_tensor_type_pointer_type = self.client.lib_ast.query(
                path=self.return_type_name
            ).pointer_type

            ptr = return_tensor_type_pointer_type(client=self.client)

            # first downcast anything primitive which is not already PyPrimitive
            (
                downcast_args,
                downcast_kwargs,
            ) = lib.python.util.downcast_args_and_kwargs(args=args, kwargs=kwargs)

            # then we convert anything which isn't a pointer into a pointer
            pointer_args, pointer_kwargs = ast.klass.pointerize_args_and_kwargs(
                args=downcast_args, kwargs=downcast_kwargs, client=self.client
            )

            if self.path_and_name is not None:
                msg = RunFunctionOrConstructorAction(
                    path=self.path_and_name,
                    args=pointer_args,
                    kwargs=pointer_kwargs,
                    id_at_location=ptr.id_at_location,
                    address=self.client.address,
                    is_static=self.is_static,
                )

                self.client.send_immediate_msg_without_reply(msg=msg)
                return ptr

        if "path" not in kwargs or "index" not in kwargs:
            traceback_and_raise(
                ValueError(
                    "AST with not client attached tries to execute remote " "function."
                )
            )
        path = kwargs["path"]
        index = kwargs["index"]

        if len(path) == index:
            return self.object_ref
        else:
            return self.attrs[path[index]](path=path, index=index + 1)

    def add_path(
        self,
        path: Union[str, List[str]],
        index: int,
        return_type_name: Optional[str] = None,
        require_pargs: bool = False,
        parg_list: List[Any] = [],
        framework_reference: Optional[ModuleType] = None,
        is_static: bool = False,
    ) -> None:
        """
        The add_path method adds new nodes in the AST based on the type of the current node and
        the type of the object to be added.

         Args:
              path (Union[List[str], str]): The path for the node in the AST to be added. Eg.
                  `syft.lib.python.List` or ["syft", "lib", "python", "List]
              index (int): The associated position in the path for the current node.
              framework_reference(Optional[ModuleType]):The python framework in which we can solve
                   the same path to obtain the python object.
              return_type_name (Optional[str]): The return type name of the given action as a
                 string (the full path to it, similar to path_and_name).
        """
        if index >= len(path) or path[index] in self.attrs:
            return
        if self.require_pargs and self.parg_list is not []:
            mod = self.object_ref(*self.parg_list)
            attr_ref = getattr(mod, path[index])
        else:
            attr_ref = getattr(self.object_ref, path[index])

        if isinstance(attr_ref, module_type):
            traceback_and_raise(
                ValueError("Module cannot be an attribute of Callable.")
            )

        self.attrs[path[index]] = ast.callable.Callable(
            path_and_name=".".join(path[: index + 1]),
            object_ref=attr_ref,
            return_type_name=return_type_name,
            require_pargs=require_pargs,
            parg_list=parg_list,
            client=self.client,
        )
