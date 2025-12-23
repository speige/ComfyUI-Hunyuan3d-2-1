# Hunyuan 3D is licensed under the TENCENT HUNYUAN NON-COMMERCIAL LICENSE AGREEMENT
# except for the third-party components listed below.
# Hunyuan 3D does not impose any additional limitations beyond what is outlined
# in the repsective licenses of these third-party components.
# Users must comply with all terms and conditions of original licenses of these third-party
# components and must ensure that the usage of the third party components adheres to
# all relevant laws and regulations.

# For avoidance of doubts, Hunyuan 3D means the large language models and
# their software and algorithms, including trained model weights, parameters (including
# optimizer states), machine-learning model code, inference-enabling code, training-enabling code,
# fine-tuning enabling code and other elements of the foregoing made publicly available
# by Tencent in accordance with TENCENT HUNYUAN COMMUNITY LICENSE AGREEMENT.

from textureGenPipeline import Hunyuan3DPaintPipeline, Hunyuan3DPaintConfig

try:
    from utils.torchvision_fix import apply_fix

    apply_fix()
except ImportError:
    print("Warning: torchvision_fix module not found, proceeding without compatibility fix")
except Exception as e:
    print(f"Warning: Failed to apply torchvision fix: {e}")


if __name__ == "__main__":

    max_num_view = 6  # can be 6 to 9
    resolution = 768  # can be 768 or 512

    # Create config with default camera angles and view weights
    camera_azims = [0, 90, 180, 270, 0, 180]
    camera_elevs = [0, 0, 0, 0, 90, -90]
    view_weights = [1, 0.1, 0.5, 0.1, 0.05, 0.05]
    ortho_scale = 1.0
    texture_size = resolution  # Use resolution as texture size

    conf = Hunyuan3DPaintConfig(resolution, camera_azims, camera_elevs, view_weights, ortho_scale, texture_size, paintpbr_path="Hunyuan3D-2.1/hunyuan3d-paintpbr-v2-1", dino_model_path="facebook/dinov2-giant")
    paint_pipeline = Hunyuan3DPaintPipeline(conf)
    output_mesh_path = paint_pipeline(mesh_path="./assets/FireElementalMonster.obj", image_path="./assets/FireElementalMonster.png")
    print(f"Output mesh path: {output_mesh_path}")
