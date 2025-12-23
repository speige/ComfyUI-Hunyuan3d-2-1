import os
import folder_paths

# Register custom model folder paths
comfy_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
hunyuan_models_path = os.path.join(comfy_path, "models", "Hunyuan3D-2.1")
facebook_model_path = os.path.join(comfy_path, "models", "facebook")

# Ensure directories exist
os.makedirs(hunyuan_models_path, exist_ok=True)
os.makedirs(facebook_model_path, exist_ok=True)

# Add the folder paths to ComfyUI
folder_paths.add_model_folder_path("Hunyuan3D-2.1", hunyuan_models_path)
folder_paths.add_model_folder_path("facebook", facebook_model_path)

from . import nodes

NODE_CLASS_MAPPINGS = nodes.NODE_CLASS_MAPPINGS
NODE_DISPLAY_NAME_MAPPINGS = nodes.NODE_DISPLAY_NAME_MAPPINGS