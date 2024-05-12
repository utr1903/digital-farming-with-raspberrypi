import logging
import time
import threading

logger = logging.getLogger(__name__)

class ActorService():

    def __init__(self, actors):
        self.actors = actors

    def run_actor(self, actor_name):
        if actor_name not in self.actors:
            logger.error(f"Given actor [{actor_name}] does not exist.")
            return False

        t = threading.Thread(target=self.run_actor_in_parallel, args=(actor_name,))
        t.start()

        return True

    def run_actor_in_parallel(self, actor_name):
        turn_on_succeeded = False
        turn_on_attempt = 0
        while turn_on_attempt < 5:
            logger.debug(f"Turning on actor [{actor_name}], attempt: {turn_on_attempt}")
            if self.actors[actor_name].turn_on() == True:
                logger.info(f"Turning on actor [{actor_name}] succeeded.")
                turn_on_succeeded = True
                break
            turn_on_attempt = turn_on_attempt + 1

        if turn_on_succeeded == False:
            logger.error(f"Turning on actor [{actor_name}] failed.")
            return

        time.sleep(2.0)

        turn_off_succeeded = False
        turn_off_attempt = 0
        while turn_off_attempt < 5:
            logger.debug(f"Turning off actor [{actor_name}], attempt: {turn_off_attempt}")
            if self.actors[actor_name].turn_off() == True:
                logger.info(f"Turning off actor [{actor_name}] succeeded.")
                turn_off_succeeded = True
                break
            turn_off_attempt = turn_off_attempt + 1

        if turn_off_succeeded == False:
            logger.error(f"Turning off actor [{actor_name}] failed.")
            return
