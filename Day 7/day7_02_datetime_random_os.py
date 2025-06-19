from datetime import datetime
import random
import os
import time

class day7_02:
    def __init__(self):
        self.cur_dir = os.path.dirname(os.path.abspath(__file__))

    def create_file(self, filepath,  file_contents: str):

        def create_path(path):
            try:
                os.makedirs(os.path.dirname(path), exist_ok=True)

            except Exception as e:
                print(f"UNABLE to create PATH DIRECTORY, an error occurred: {e}")
        
        create_path(filepath)

        with open(filepath, 'w') as file:
            file.write(file_contents)

        


    def get_system_state(self):
        states = ['idle', 'running', 'error', 'maintenance']
        return random.choice(states)
    
    def log_generate(self):
        dt = datetime.now()
        f_name = f'log_{dt.strftime("%Y-%m-%dT%H-%M-%S")}.txt'
        f_path = os.path.join(self.cur_dir,'logs',f_name)
        contents = f'System state = {self.get_system_state()} at {datetime.isoformat(dt)}'

        self.create_file(f_path,contents)

if __name__ == '__main__':
    task = day7_02()

    while True:
        task.log_generate()
        time.sleep(5)