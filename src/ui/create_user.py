from tkinter import StringVar, Tk, ttk, constants, messagebox
from services.shift_app_service import InvalidPassword, UsernameExistsError, UsernameTooShortError, NoRoleError


class CreateUserUi:
    """Class for user creatioon view
    """

    def __init__(self, root, handle_create_user, handle_login, service):
        """Constructor for user creation view

        Args:
            root (Tk()): TK() window from the ui
            handle_create_user (function): Function that handles the create user view
            handle_login (function): Function that handles the login view
            service (class): The service the whole ui uses
        """
        self._root = root
        self._handle_create_user = handle_create_user
        self._handle_login = handle_login
        self._frame = None
        self._role = StringVar()
        self._username_entry = StringVar()
        self._password_entry = StringVar()
        self._service = service

        self._base()

    def pack(self):
        """Shows the view
        """
        self._frame.pack(fill=constants.X)

    def destroy(self):
        """Closes the view
        """
        self._frame.destroy()
    
    def _handle_back_button(self):
        self._handle_login()

    def _handle_button_click(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self._role.get()
        try:
            self._service.create_user(
                username=username, password=password, role=role)
            messagebox.showinfo(title="User created",
                                message="User created succesfully!")

        except UsernameTooShortError:
            messagebox.showerror(title="Username too short",
                                 message="Username is too short, please provide a username longer than 2 characters"
                                 )

        except NoRoleError:
            messagebox.showerror(title="No role chosen",
                                 message="Please choose a role")

        except InvalidPassword:
            messagebox.showinfo(
                title="Invalid Password", message="Password should be over 8 characters, include at least one upper- and lowercase letter, a special character and a number"
            )

        except UsernameExistsError:
            messagebox.showerror(title="Username exists",
                                 message=f"User {username} already exists!"
                                 )


    def _base(self):
        self._frame = ttk.Frame(master=self._root)

        header = ttk.Label(master=self._frame, text="Create a user")
        header.grid(row=0, column=0)

        username_header = ttk.Label(master=self._frame, text="Username")
        username_header.grid(row=2, column=0)

        self.username_entry = ttk.Entry(
            master=self._frame, textvariable=self._username_entry)

        self.username_entry.grid(row=3, column=0)

        password_header = ttk.Label(master=self._frame, text="Password")
        password_header.grid(row=4, column=0)

        self.password_entry = ttk.Entry(
            master=self._frame, textvariable=self._password_entry)
        self.password_entry.grid(row=5, column=0)

        self.employee_button = ttk.Radiobutton(
            master=self._frame, text="Employee", variable=self._role, value="Employee")
        self.employee_button.grid(row=7, column=0)

        self.employer_button = ttk.Radiobutton(
            master=self._frame, text="Employer", variable=self._role, value="Employer")
        self.employer_button.grid(row=8, column=0)

        create_button = ttk.Button(
            master=self._frame, text="Create", command=self._handle_button_click)
        create_button.grid(row=10, column=0)

        back_button = ttk.Button(
            master=self._frame, text="Back", command=self._handle_back_button
        )
        back_button.grid(row=12, column=0)

