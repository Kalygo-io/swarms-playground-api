from src.core.local_swarms.swarms.models.base_embedding_model import BaseEmbeddingModel
from src.core.local_swarms.swarms.models.base_llm import BaseLLM  # noqa: E402
# from src.core.local_swarms.swarms.models.base_multimodal_model import BaseMultiModalModel
# from src.core.local_swarms.swarms.models.fuyu import Fuyu  # noqa: E402
# from src.core.local_swarms.swarms.models.gpt4_vision_api import GPT4VisionAPI  # noqa: E402
# from src.core.local_swarms.swarms.models.huggingface import HuggingfaceLLM  # noqa: E402
# from src.core.local_swarms.swarms.models.idefics import Idefics  # noqa: E402
# from src.core.local_swarms.swarms.models.kosmos_two import Kosmos  # noqa: E402
# from src.core.local_swarms.swarms.models.layoutlm_document_qa import LayoutLMDocumentQA
# from src.core.local_swarms.swarms.models.llama3_hosted import llama3Hosted
# from src.core.local_swarms.swarms.models.llava import LavaMultiModal  # noqa: E402
# from src.core.local_swarms.swarms.models.nougat import Nougat  # noqa: E402
# from src.core.local_swarms.swarms.models.openai_embeddings import OpenAIEmbeddings
# from src.core.local_swarms.swarms.models.openai_tts import OpenAITTS  # noqa: E402
# from src.core.local_swarms.swarms.models.palm import GooglePalm as Palm  # noqa: E402
from src.core.local_swarms.swarms.models.popular_llms import Anthropic as Anthropic
# from src.core.local_swarms.swarms.models.popular_llms import (
#     AzureOpenAILLM as AzureOpenAI,
# )
# from src.core.local_swarms.swarms.models.popular_llms import (
#     CohereChat as Cohere,
# )
# from src.core.local_swarms.swarms.models.popular_llms import OctoAIChat
from src.core.local_swarms.swarms.models.popular_llms import (
    OpenAIChatLLM as OpenAIChat,
)
from src.core.local_swarms.swarms.models.popular_llms import (
    OpenAILLM as OpenAI,
)
# from src.core.local_swarms.swarms.models.popular_llms import ReplicateChat as Replicate
# from src.core.local_swarms.swarms.models.qwen import QwenVLMultiModal  # noqa: E402
# from src.core.local_swarms.swarms.models.sampling_params import SamplingParams, SamplingType
# from src.core.local_swarms.swarms.models.together import TogetherLLM  # noqa: E402
# from src.core.local_swarms.swarms.models.model_types import (  # noqa: E402
#     AudioModality,
#     ImageModality,
#     MultimodalData,
#     TextModality,
#     VideoModality,
# )
# from src.core.local_swarms.swarms.models.vilt import Vilt  # noqa: E402
# from src.core.local_swarms.swarms.models.popular_llms import FireWorksAI
# from src.core.local_swarms.swarms.models.openai_function_caller import OpenAIFunctionCaller

__all__ = [
    "BaseEmbeddingModel",
    "BaseLLM",
#     "BaseMultiModalModel",
#     "Fuyu",
#     "GPT4VisionAPI",
#     "HuggingfaceLLM",
#     "Idefics",
#     "Kosmos",
#     "LayoutLMDocumentQA",
#     "LavaMultiModal",
#     "Nougat",
#     "Palm",
#     "OpenAITTS",
    "Anthropic",
#     "AzureOpenAI",
#     "Cohere",
    "OpenAIChat",
    "OpenAI",
#     "OctoAIChat",
#     "QwenVLMultiModal",
#     "Replicate",
#     "SamplingParams",
#     "SamplingType",
#     "TogetherLLM",
#     "AudioModality",
#     "ImageModality",
#     "MultimodalData",
#     "TextModality",
#     "VideoModality",
#     "Vilt",
#     "OpenAIEmbeddings",
#     "llama3Hosted",
#     "FireWorksAI",
#     "OpenAIFunctionCaller",
]
