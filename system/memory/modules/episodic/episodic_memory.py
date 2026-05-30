import json

from pathlib import Path

from datetime import datetime

from config.paths import BASE_DIR


class EpisodicMemory:

    def __init__(self):

        self.memory_path = (

            Path(BASE_DIR) /

            "system/memory/history/episodic_memory.json"
        )

        self.initialize_memory()

    # ========================================
    # INITIALIZE MEMORY
    # ========================================

    def initialize_memory(self):

        if not self.memory_path.exists():

            with open(
                self.memory_path,
                "w"
            ) as f:

                json.dump([], f)

            print(
                "\nEpisodic memory initialized ✅"
            )

    # ========================================
    # LOAD MEMORY
    # ========================================

    def load_memory(self):

        with open(
            self.memory_path,
            "r"
        ) as f:

            memory = json.load(f)

        return memory

    # ========================================
    # STORE EPISODE
    # ========================================

    def store_episode(

        self,
        signal,
        workflow,
        outcome

    ):

        memory = self.load_memory()

        episode = {

            "signal":
                signal,

            "workflow":
                workflow,

            "outcome":
                outcome,

            "timestamp":
                str(datetime.now())
        }

        memory.append(episode)

        with open(
            self.memory_path,
            "w"
        ) as f:

            json.dump(
                memory,
                f,
                indent=4
            )

        print(
            "\nEpisode stored ✅"
        )

        return episode