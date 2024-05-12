import logging

from actors import base

logger = logging.getLogger(__name__)

class ActorMock(base.ActorBase):

    def __init__(self, actor_name):
        super().__init__(actor_name)

    def turn_on(self):
        logger.info(f"Turning on actor [{self.get_actor_name()}]...")
        try:
            logger.info(f"Turning on actor [{self.get_actor_name()}] succeeded.")
            return True
        except Exception as e:
            logger.error(f"Turning on actor [{self.get_actor_name()}] failed: {e}")
            return False

    def turn_off(self):
        logger.info(f"Turning off actor [{self.get_actor_name()}]...")
        try:
            logger.info(f"Turning off actor [{self.get_actor_name()}] succeeded.")
            return True
        except Exception as e:
            logger.error(f"Turning off actor [{self.get_actor_name()}] failed: {e}")
            return False