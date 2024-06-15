import typing as t

from composio.core.local import Action, Tool

from .actions import ScreenCapture, Notify

class System(Tool):
    """
    Mathematical Tools for LLM
    """

    def actions(self) -> list[t.Type[Action]]:
        return [ScreenCapture, Notify]

    def triggers(self) -> list:
        return []
