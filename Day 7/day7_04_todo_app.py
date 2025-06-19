import os
import json


class TODO:
    def __init__(self):
        try:
            self.cur_dir = os.path.dirname(os.path.abspath(__file__))
            self.filepath = os.path.join(self.cur_dir,'TO-DO','TODO.json')
            
            self.file = None
            self.data = None

            self.read_json()
            
        except FileNotFoundError as fe:
            self.create_file(self.filepath,{'app_name':'TODO App','task':[]})
            self.read_json()

        except Exception as e:
            print(e)
        finally:
            if self.data:
                # print(self.data)
                self.controller()
            

    def create_file(self,filepath: str,file_contents):
        def create_path(path):
            try:
                os.makedirs(os.path.dirname(path), exist_ok=True)

            except Exception as e:
                print(f"UNABLE to create PATH DIRECTORY, an error occurred: {e}")
        
        create_path(filepath)

        with open(filepath, 'w') as file:
            json.dump(file_contents, file,indent=4)

    def read_json(self):
        self.file = open(self.filepath,'r+')
        self.data = json.load(self.file)
    
    def close_json(self):
        self.file.seek(0)
        json.dump(self.data,self.file, indent=4)
        self.file.truncate()

    def show_task(self):
        print('\n','TO-DO List'.center(len('TO-DO List')+10,'-'))
        if len(self.data['task']):
            for idx,task in enumerate(self.data['task'], start=1):
                print(f'{idx}. [{'✅' if task['status'] else '  ' }] {task['label']}')
        else:
            print("List is EMPTY")
        # pass

    def controller(self):
        try:
            in_control = True
            option = None
            print(f''' 
    1. Add Task
    2. Mark Done
    3. Mark Pending
    4. Delete Task
    5. Clear List
    0. Exit
    ''')
            while in_control:
                self.show_task()
                option = input('\nOption =>  ')

                if option == '1':
                    self.add_task()
                elif option == '2':
                    self.mark_done()
                elif option == '3':
                    self.mark_pending()
                elif option == '4':
                    self.del_task()
                elif option == '5':
                    self.clr_list()
                elif option == '0':
                    self.close_json()
                    print("Exit Successfully")
                    in_control = False
                    exit()
                else:
                    print('INVALID CHOICE, try again...')
        except KeyboardInterrupt:
            print("\nKeyboard Escape INITIATED!!")
        except Exception as e:
            print(e)
        finally:
            self.close_json()

    def add_task(self):
        t_name = None
        t_name = input('Enter Task: ')
        self.data['task'].append({'label':t_name, 'status': False})

    def mark_done(self):
        t_id = None
        t_id = int(input('Mark DONE, id: '))
        [x.update({'status':True}) for idx,x  in enumerate(self.data['task'], start=1) if idx == t_id]

    def mark_pending(self):
        t_id = None
        t_id = int(input('Mark PENDING, id: '))
        [x.update({'status':False}) for idx,x  in enumerate(self.data['task'], start=1) if idx == t_id]

    def del_task(self):
        t_id = None
        t_id = int(input('DEL Task, id: '))
        if input(f"Confirm DELETE task id : {t_id} \nY/N (YES/NO):").lower() == 'y':
            self.data['task'] = [x for idx,x in enumerate(self.data['task'], start=1) if idx != t_id]
        else:
            print("Action Denied")

    def clr_list(self):
        if input(f"Confirm CLEAR List: \nY/N (YES/NO):").lower() == 'y':
            self.data['task'].clear()
        else:
            print("Action Denied")

if __name__ == '__main__':

    TODO()