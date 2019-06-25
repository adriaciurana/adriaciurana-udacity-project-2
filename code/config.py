import os
import torch
class Config:
	"""
		PATHS
	"""
	CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
	PROJECT_PATH = os.path.dirname(CURRENT_PATH)
	
	ENVS_PATH = os.path.join(PROJECT_PATH, "envs")
	CHECKPOINT_PATH = os.path.join(PROJECT_PATH, "checkpoints")
	MODELS_PATH = os.path.join(PROJECT_PATH, "models")
	
	CONTINUOUS_ENV_PATH = os.path.join(ENVS_PATH, "one", "Reacher.x86_64")
	CHECKPOINT_CONTINUOUS_PATH = os.path.join(CHECKPOINT_PATH, "one")
	MODEL_CONTINUOUS_PATH = os.path.join(MODELS_PATH, "one")

	CONTINUOUS_TWENTY_ENV_PATH = os.path.join(ENVS_PATH, "twenty", "Reacher.x86_64")
	CHECKPOINT_CONTINUOUS_TWENTY_PATH = os.path.join(CHECKPOINT_PATH, "twenty")
	MODEL_CONTINUOUS_TWENTY_PATH = os.path.join(MODELS_PATH, "twenty")

	"""
		TORCH CONFIG
	"""
	DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

	"""
		 TRAINING PARAMETERS
	"""
	ENABLE_TRAIN = True
	SELECTED_ENV = 'twenty'

	BUFFER_SIZE = int(1e6)  # replay buffer size
	BATCH_SIZE = 5000       # minibatch size
	GAMMA = 0.99            # discount factor
	TAU = 1e-3              # for soft update of target parameters
	LR_ACTOR = 1e-4         # learning rate of the actor 
	LR_CRITIC = 1e-3        # learning rate of the critic
	WEIGHT_DECAY = 0        # L2 weight decay
	LEARN_INTERVAL = None     # Interval of learning, for continuous put None or 1