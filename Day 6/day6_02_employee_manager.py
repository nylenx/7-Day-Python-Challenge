class employee:
    def __init__(self,name:str,emp_id:str,dept:str):
        self.name = name
        self.emp_id = emp_id
        self.dept = dept
        print("Employee Created")
    
    def show_details(self):
        print(
f'''
Name : {self.name}
Emp ID : {self.emp_id}
Department : {self.dept}
''')
        
class manager(employee):
    def __init__(self,name,emp_id,dept,team_size):
        super().__init__(name,emp_id,dept)
        self.team_size = team_size
        print("Promoted to Manager")
    
    def show_details(self):
        super().show_details()
        print(f'Team size: {self.team_size}')

if __name__ == '__main__':
    emp1 = employee('Rehan','emp_017','Accounts')
    emp1.show_details()

    mgr1 = manager('Aadesh','emp_011','Sales','10')
    mgr1.show_details()