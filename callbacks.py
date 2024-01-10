from typing import Dict, Any, List, Optional
from uuid import UUID

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.outputs import LLMResult


class AgentCallbackHandler(BaseCallbackHandler):
    def on_llm_start(
        self,
        serialized: Dict[str, Any],
        prompts: List[str],
        **kwargs: Any,
    ) -> Any:
        """Run when llm starts running"""
        print(f"*** Promops to element was*** \n {prompts[0]}")
        print("*******")

    def on_llm_end(
        self,
        response: LLMResult,
        **kwargs: Any,
    ) -> Any:
        """Run when llm ends running"""
        print(f"*** LLM response: ***\n {response.generations[0][0].text}")
        print("*******")
