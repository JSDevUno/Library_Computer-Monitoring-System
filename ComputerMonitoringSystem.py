import PySimpleGUI as sg
import pandas as pd
import datetime
import openpyxl
import os
import sys


def get_image_path(filename):
    if getattr(sys, 'frozen', False):
        # If running as a frozen executable
        base_path = sys._MEIPASS
    else:
        # If running as a script
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, 'icons', filename)


def create_main_menu_layout():
    # Define custom border color and radius settings (simulated)
    border_color = 'lightblue'
    border_radius = 2  # Simulated radius for rounded corners

    def create_button_with_frame(button_text, key, image_filename):
        return sg.Frame(
            '',
            [[sg.Button("", key=key, size=(30, 3), image_filename=get_image_path(image_filename),
                        image_size=(400, 60), border_width=0)]],
            background_color=border_color,
            border_width=border_radius,
            element_justification='center',
            pad=((border_radius, border_radius), (border_radius, border_radius))
        )

    layout = [
        [sg.Text("Library Computer Monitoring System", size=(40, 1), font=("Helvetica", 25), justification="center")],
        [sg.Column([
            [sg.Text("Register Users:", font=("Helvetica", 14))],
            [create_button_with_frame("Register Users", "-REGISTER-", "icons8_add_user_group_man_woman_40px.png")]
        ], justification="center")],
        [sg.Column([
            [sg.Text("Users:", font=("Helvetica", 14))],
            [create_button_with_frame("Manage Users", "-MANAGE-", "icons8_team_40px.png")]
        ], justification="center")],
        [sg.Column([
            [sg.Text("Manage PC Users:", font=("Helvetica", 14))],
            [create_button_with_frame("Manage PC Users", "-PC_USERS-", "icons8_windows_client_40px.png")]
        ], justification="center")],
        [sg.Column([
            [sg.Text("Manage User Logs:", font=("Helvetica", 14))],
            [create_button_with_frame("Manage User Logs", "-MANAGE_USER_LOGS-",
                                      "icons8_checked_user_male_40px.png")]
        ], justification="center")],
        [sg.Column([
            [sg.Text("Generate Report:", font=("Helvetica", 14))],
            [create_button_with_frame("Generate Report", "-GENERATE_REPORT-", "icons8_file_40px.png")]
        ], justification="center")],
        [sg.Column([
            [sg.Text("Exit:", font=("Helvetica", 14))],
            [create_button_with_frame("Exit", "-EXIT-", "icons8_exit_40px.png")]
        ], justification="center")]
    ]

    return layout


def create_time_out_options_layout():
    layout = [
        [sg.Text("Time Out Options", size=(40, 1), font=("Helvetica", 25), justification="center")],
        [sg.Button("Manual Time-Out", key="-MANUAL_TIMEOUT-", size=(30, 3), font=("Helvetica", 14))],
        [sg.Button("Identify User Login", key="-IDENTIFY_LOGIN-", size=(30, 3), font=("Helvetica", 14))],
        [sg.Button("Back", key="-BACK-", size=(30, 3), font=("Helvetica", 14))]
    ]
    return layout


def create_manage_pc_users_layout():
    pc_numbers = list(map(str, range(1, 11)))
    staff_list = ['D. Navarrete', 'K. Padre', 'S. Pillos']

    # Define background colors for each column
    column_bg_color = '#f0f0f0'  # Light grey background for columns

    layout = [
        [sg.Text("Manage PC Users", size=(40, 1), font=("Helvetica", 25), justification="center")],

        # Group PC Number and Search By
        [sg.Column([
            [sg.Text("PC Number:", size=(15, 1), font=("Helvetica", 18), justification='center',
                     background_color='#1570a7'),
             sg.Combo(pc_numbers, key='pc_number', size=(20, 1), font=("Helvetica", 18))],
            [sg.Text("Search By:", size=(15, 1), font=("Helvetica", 18), justification='center',
                     background_color='#1570a7'),
             sg.Combo(['Student Number', 'Student Name'], key='search_criteria', size=(20, 1), font=("Helvetica", 18),
                      default_value='Student Number')]
        ], background_color=column_bg_color, pad=(10, 5), element_justification='left')],

        # Group Search Field and Button
        [sg.Column([
            [sg.Text("Search Field:", size=(15, 1), font=("Helvetica", 18), justification='center',
                     background_color='#1570a7'),
             sg.InputText(key='search_field', size=(20, 1), font=("Helvetica", 18)),
             sg.Button("Search", size=(10, 1), font=("Helvetica", 18))]
        ], background_color=column_bg_color, pad=(10, 5), element_justification='center')],

        # PC User Display with Background Color
        [sg.Column([
            [sg.Text("PC User:", size=(15, 1), font=("Helvetica", 18), justification='center',
                     background_color='#1570a7'),
             sg.Text("", size=(30, 1), key='student_display', font=("Helvetica", 18),
                     background_color='#283b5b', text_color='white', pad=(5, 5))]
        ], background_color=column_bg_color, pad=(10, 5), element_justification='center')],

        # Group Date Selection
        [sg.Column([
            [sg.Text("Date:", size=(15, 1), font=("Helvetica", 18), justification='center', background_color='#1570a7'),
             sg.Combo(list(range(1, 13)), key='month', default_value=datetime.datetime.now().month, size=(5, 1),
                      font=("Helvetica", 18)),
             sg.Combo(list(range(1, 32)), key='day', default_value=datetime.datetime.now().day, size=(5, 1),
                      font=("Helvetica", 18)),
             sg.Combo(list(range(datetime.datetime.now().year - 5, datetime.datetime.now().year + 1)), key='year',
                      default_value=datetime.datetime.now().year, size=(8, 1), font=("Helvetica", 18))]
        ], background_color=column_bg_color, pad=(10, 5), element_justification='center')],

        # Group Time In
        [sg.Column([
            [sg.Text("Time In:", size=(15, 1), font=("Helvetica", 18), justification='center',
                     background_color='#1570a7'),
             sg.Combo(list(range(1, 13)), key='time_in_hour', size=(5, 1), font=("Helvetica", 18)),
             sg.Combo(['00', '15', '30', '45'], key='time_in_minute', size=(5, 1), font=("Helvetica", 18)),
             sg.Combo(['AM', 'PM'], key='time_in_am_pm', size=(5, 1), font=("Helvetica", 18)),
             sg.Button("Current Time In", size=(15, 1), font=("Helvetica", 18))]
        ], background_color=column_bg_color, pad=(10, 5), element_justification='center')],

        # Group Time Out
        [sg.Column([
            [sg.Text("Time Out:", size=(15, 1), font=("Helvetica", 18), justification='center',
                     background_color='#1570a7'),
             sg.Combo(list(range(1, 13)), key='time_out_hour', size=(5, 1), font=("Helvetica", 18)),
             sg.Combo(['00', '15', '30', '45'], key='time_out_minute', size=(5, 1), font=("Helvetica", 18)),
             sg.Combo(['AM', 'PM'], key='time_out_am_pm', size=(5, 1), font=("Helvetica", 18)),
             sg.Button("Time Out", size=(15, 1), font=("Helvetica", 18))]
        ], background_color=column_bg_color, pad=(10, 5), element_justification='center')],

        # Assigned Staff
        [sg.Column([
            [sg.Text("Assigned Staff:", size=(12, 1), font=("Helvetica", 18), justification='center',
                     background_color='#1570a7'),
             sg.Combo(staff_list, key='assigned_staff', size=(20, 1), font=("Helvetica", 18))]
        ], background_color=column_bg_color, pad=(10, 5), element_justification='center')],

        # Action Buttons
        [sg.Column([
            [sg.Button("Approve", size=(15, 1), font=("Helvetica", 18)),
             sg.Button("Back", size=(15, 1), font=("Helvetica", 18))]
        ], background_color=column_bg_color, pad=(10, 10), element_justification='center')]
    ]

    # Center the layout
    space_layout = [
        [sg.Column(layout, element_justification='center', pad=(20, 20))]
    ]

    return space_layout


def save_pc_user_data(data):
    try:
        df = pd.read_excel('pc_users_history_log.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['PC Number', 'User Name', 'User Number',
                                   'Course', 'Date', 'Time In', 'Time Out', 'Assigned Staff'])

    # Remove 'Search Field' from data
    new_data = pd.DataFrame([{
        key: value for key, value in data.items() if key != 'Search Field'
    }])

    df = pd.concat([df, new_data], ignore_index=True)

    with pd.ExcelWriter('pc_users_history_log.xlsx', engine='openpyxl', mode='w') as writer:
        df.to_excel(writer, index=False, header=True, startrow=0, startcol=0)


def save_user_logs_data(data):
    try:
        df = pd.read_excel('user_logs.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['PC Number', 'User Name', 'User Number',
                                   'Course', 'Date', 'Time In', 'Time Out', 'Assigned Staff'])

        # Remove 'Search Field' from data
    new_data = pd.DataFrame([{
        key: value for key, value in data.items() if key != 'Search Field'
    }])

    df = pd.concat([df, new_data], ignore_index=True)

    with pd.ExcelWriter('user_logs.xlsx', engine='openpyxl', mode='w') as writer:
        df.to_excel(writer, index=False, header=True, startrow=0, startcol=0)


def count_users_by_course_and_date():
    try:
        df = pd.read_excel('pc_users_history_log.xlsx')
        count_data = df.groupby(['Course', 'Date']).size().unstack(fill_value=0)
        count_data.to_excel('user_count_by_course_and_date.xlsx', index=True)
    except FileNotFoundError:
        sg.popup_error("No PC user history log found. Please use Manage PC Users to create entries.")


def create_manage_user_logs_layout():
    # Set initial values and headings for the table
    try:
        user_logs_df = pd.read_excel('user_logs.xlsx', dtype={'PC Number': str})
        user_logs_data = user_logs_df.values.tolist()
        headings = user_logs_df.columns.tolist()
    except FileNotFoundError:
        user_logs_data = []
        headings = ['PC Number', 'User Name', 'User Number', 'Course', 'Date', 'Time In', 'Time Out', 'Assigned Staff']

    # Define the layout
    layout = [
        [sg.Text("Manage User Logs", size=(30, 1), font=("Helvetica", 20), justification="center", expand_x=True)],
        [sg.Table(values=user_logs_data,
                  headings=headings,
                  key='user_logs_table',
                  display_row_numbers=False,
                  auto_size_columns=True,
                  num_rows=10,
                  enable_events=True,
                  justification='center')],
        [sg.Button("Delete Row", key="-DELETE_ROW-"), sg.Button("Back")]
    ]

    return layout


def create_manage_students_layout():
    try:
        df = pd.read_excel('users_data.xlsx')
        header_list = ['User Name', 'User Number', 'Course']
        table_data = df.to_numpy().tolist()
    except FileNotFoundError:
        header_list = ['User Name', 'User Number', 'Course']
        table_data = []

    # Define column widths in pixels
    column_widths = [20, 20, 20]  # Adjust as needed

    layout = [
        [sg.Text("Manage Users", size=(40, 1), font=("Helvetica", 25), justification="center")],

        [sg.Column([
            [sg.Table(values=table_data, headings=header_list,
                      auto_size_columns=False,
                      display_row_numbers=True,
                      justification='center',
                      key='-TABLE-',
                      font=("Helvetica", 18),
                      num_rows=10,
                      alternating_row_color='black',
                      row_height=30,
                      pad=(0, 0),
                      col_widths=column_widths,  # Set specific column widths
                      expand_x=True,  # Allow the table to expand horizontally
                      vertical_scroll_only=True)]  # Add vertical scrollbars
        ], background_color='#FFFFFF', pad=(20, 20))],

        [sg.Button("Back", size=(10, 2), font=("Helvetica", 18), button_color=("#ffffff", "#283b5b"))]
    ]

    # Center column and add padding
    space_layout = [
        [sg.Column(layout, element_justification='center', pad=(20, 20))]
    ]

    return space_layout


def generate_report(selected_month, selected_year):
    try:
        if not selected_month or not selected_month.isalpha() or not selected_year.isdigit():
            sg.popup_error("Invalid selection. Please choose a valid month and year.")
            return

        # Extract month and year from the selected values
        month_name, year = selected_month, int(selected_year)

        pc_user_data = pd.read_excel('pc_users_history_log.xlsx')

        # Convert 'Date' column to datetime
        pc_user_data['Date'] = pd.to_datetime(pc_user_data['Date'], errors='coerce')

        # Filter data for the selected month and year
        filtered_data = pc_user_data[
            (pc_user_data['Date'].dt.month == datetime.datetime.strptime(month_name, '%B').month) &
            (pc_user_data['Date'].dt.year == year)
            ]

        if filtered_data.empty:
            sg.popup_annoying("No data found for the selected month and year.", title="Warning")
            return

        # List of specified courses
        specified_courses = ['BSEE', 'BSCpE', 'BSInfotech', 'BSCS', 'BSE', 'BTVTED', 'BSIT', 'BSHM', 'BSBM', 'JHS',
                             'SHS', 'TCP', 'FACULTY', 'VISITOR/S']

        # Create a DataFrame for the report
        report_df = pd.DataFrame(index=range(1, 32), columns=['Date'] + specified_courses + ['TOTAL'])

        report_df['Date'] = [f"{month_name[:3]}/{day}" for day in range(1, 32)]

        # Initialize counts to 0
        report_df.iloc[:, 1:-1] = 0

        # Convert columns to numeric
        report_df.iloc[:, 1:-1] = report_df.iloc[:, 1:-1].apply(pd.to_numeric, errors='coerce')

        # Compute the number of students for each course on each date
        for index, row in filtered_data.iterrows():
            course = row['Course']
            if course in specified_courses:
                date_day = row['Date'].day
                report_df.at[date_day, course] += 1

        # Compute the total for each date
        report_df['TOTAL'] = report_df.iloc[:, 1:-1].sum(axis=1)

        # Calculate the sum of each column (course) and put it in the "TOTAL" row
        report_df.loc['TOTAL', specified_courses] = report_df[specified_courses].sum()

        # Calculate the sum of the "TOTAL" column
        total_sum = report_df['TOTAL'].sum()

        # Add the total sum to the last row of the "TOTAL" column
        report_df.at['TOTAL', 'TOTAL'] = total_sum

        # Add 'TOTAL' in the first column of the last row
        report_df.at['TOTAL', 'Date'] = 'TOTAL'

        # Replace 0 values with empty strings
        report_df.replace(0, '', inplace=True)

        # Modify the file name to include the selected month and year
        report_path = f'Report_{month_name}_{year}.xlsx'

        report_df.to_excel(report_path, index=False, na_rep='')

        sg.popup(f"Report generated successfully!\nSaved as {report_path}", title="Success")
    except FileNotFoundError:
        sg.popup_error("No PC user history log found. Please use Manage PC Users to create entries.", title="Error")


def create_generate_report_layout():
    # Get the current year and month
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().strftime('%B')

    # List of months in a readable format for the current year
    readable_months = [datetime.date(current_year, i, 1).strftime('%B') for i in range(1, 13)]

    # List of years for the Combo box
    year_list = list(range(current_year - 5, current_year + 6))  # You can adjust the range as needed

    column_bg_color = '#f0f0f0'  # Light grey background for columns

    layout = [
        [sg.Text("Generate Report", size=(40, 1), font=("Helvetica", 30), justification="center")],

        # Select Month
        [sg.Column([
            [sg.Text("Select Month:", size=(15, 1), font=("Helvetica", 18), justification='center',
                     background_color='#1570a7'),
             sg.Combo(readable_months, default_value=current_month, key='selected_month', size=(20, 1),
                      font=("Helvetica", 18))]
        ], background_color=column_bg_color, pad=(10, 5), element_justification='left')],

        # Select Year
        [sg.Column([
            [sg.Text("Select Year:", size=(15, 1), font=("Helvetica", 18), justification='center',
                     background_color='#1570a7'),
             sg.Combo(year_list, default_value=current_year, key='selected_year', size=(20, 1), font=("Helvetica", 18))]
        ], background_color=column_bg_color, pad=(10, 5), element_justification='left')],

        # Action Buttons
        [sg.Column([
            [sg.Button("Generate Report", size=(15, 1), font=("Helvetica", 18)),
             sg.Button("Back", size=(15, 1), font=("Helvetica", 18))]
        ], background_color=column_bg_color, pad=(10, 10), element_justification='center')]
    ]

    # Center the layout
    space_layout = [
        [sg.Column(layout, element_justification='center', pad=(20, 20))]
    ]
    return space_layout


def create_register_student_layout():
    courses = ['BSEE', 'BSCpE', 'BSInfotech', 'BSCS', 'BSE', 'BTVTED', 'BSIT', 'BSHM', 'BSBM', 'JHS', 'SHS', 'TCP',
               'FACULTY', 'VISITOR/S']

    # Define colors to match the buttons
    background_color = '#283b5b'  # Light grey for the background color of columns
    button_color = '#E0E0E0'  # Blue for the button background

    layout = [
        [sg.Text("Register User", size=(40, 1), font=("Helvetica", 35), justification="center")],

        [sg.Column([
            [sg.Text("User Name:", size=(15, 1), font=("Helvetica", 20), justification='left',
                     background_color=background_color)],
            [sg.InputText(key='student_name', size=(30, 1), font=("Helvetica", 18))]
        ], background_color=background_color, pad=(10, 5), element_justification='left')],

        [sg.Column([
            [sg.Text("User Number:", size=(15, 1), font=("Helvetica", 20), justification='left',
                     background_color=background_color)],
            [sg.InputText(key='student_number', size=(30, 1), font=("Helvetica", 18))]
        ], background_color=background_color, pad=(10, 5), element_justification='left')],

        [sg.Column([
            [sg.Text("Course:", size=(15, 1), font=("Helvetica", 20), justification='left',
                     background_color=background_color)],
            [sg.Combo(courses, key='course', size=(29, 1), font=("Helvetica", 18))]
        ], background_color=background_color, pad=(10, 5), element_justification='left')],

        [sg.Column([
            [sg.Button("Save", size=(15, 2), font=("Helvetica", 18),
                       button_color=(background_color, button_color))],
            [sg.Button("Cancel", size=(15, 2), font=("Helvetica", 18),
                       button_color=(background_color, button_color))]
        ], background_color=background_color, pad=(10, 10), element_justification='center')]
    ]

    # Adding padding and aligning the layout
    layout_with_padding = [
        [sg.Column(layout, element_justification='center', pad=(10, 10))]
    ]

    return layout_with_padding


def validate_input(values):
    if not values['student_name'].replace(' ', '').isalpha():
        sg.popup_error("Invalid input for User Name. Please use only letters, spaces, and special characters.")
        return False
    elif not values['student_number'].isdigit():
        sg.popup_error("Invalid input for User Number. Please use only numbers.")
        return False
    elif values['course'] not in ['BSEE', 'BSCpE', 'BSInfotech', 'BSCS', 'BSE', 'BTVTED', 'BSIT', 'BSHM', 'BSBM', 'JHS',
                                  'SHS', 'TCP', 'FACULTY', 'VISITOR/S']:
        sg.popup_error("Invalid input for Course. Please select a valid option from the dropdown.")
        return False
    return True


def save_student_data(data):
    try:
        df = pd.read_excel('users_data.xlsx')
    except FileNotFoundError:
        df = pd.DataFrame(columns=['User Name', 'User Number', 'Course'])

    new_data = pd.DataFrame([data])

    # Convert 'Student Number' to numeric type
    new_data['User Number'] = pd.to_numeric(new_data['User Number'], errors='coerce')

    df = pd.concat([df, new_data], ignore_index=True)

    with pd.ExcelWriter('users_data.xlsx', engine='openpyxl', mode='w') as writer:
        df.to_excel(writer, index=False, header=True, startrow=0, startcol=0)


def main():
    # Load existing student data from Excel if it exists
    try:
        student_data = pd.read_excel('users_data.xlsx').to_dict(orient='records')
    except FileNotFoundError:
        student_data = []

    pc_user_data = []

    window = sg.Window("Library Computer Program", create_main_menu_layout())

    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == "-EXIT-":
            break

        elif event == "-GENERATE_REPORT-":
            # Create a new window for report generation
            window.hide()
            generate_report_layout = create_generate_report_layout()
            generate_report_window = sg.Window("Generate Report", generate_report_layout)

            while True:
                event_generate_report, values_generate_report = generate_report_window.read()

                if event_generate_report == sg.WINDOW_CLOSED or event_generate_report == "Back":
                    generate_report_window.close()
                    window.un_hide()
                    break
                elif event_generate_report == "Generate Report":
                    selected_month = values_generate_report['selected_month']
                    selected_year = str(values_generate_report['selected_year'])
                    generate_report(selected_month, selected_year)

            generate_report_window.close()

        elif event == "-REGISTER-":
            window.hide()
            registration_layout = create_register_student_layout()
            registration_window = sg.Window("Register User", registration_layout)

            while True:
                event_reg, values_reg = registration_window.read()

                if event_reg == sg.WINDOW_CLOSED or event_reg == "Cancel":
                    break
                elif event_reg == "Save":
                    if validate_input(values_reg):
                        # Check if the user number already exists in the DataFrame
                        existing_data = pd.read_excel('users_data.xlsx', dtype={'User Number': str})
                        if values_reg['student_number'] in existing_data['User Number'].values:
                            sg.popup_error(
                                f"User with User Number {values_reg['student_number']} already exists. Please enter a different User Number.")
                        else:
                            student_data.append({
                                'User Name': values_reg['student_name'],
                                'User Number': values_reg['student_number'],
                                'Course': values_reg['course']
                            })
                            save_student_data(student_data[-1])  # Save the last added student
                            sg.popup("User registered successfully!")
                            break  # Break out of the registration loop

            registration_window.close()
            window.un_hide()

        elif event == "-MANAGE-":
            window.hide()
            manage_layout = create_manage_students_layout()
            manage_window = sg.Window("Manage Users", manage_layout)

            while True:
                event_manage, values_manage = manage_window.read()

                if event_manage == sg.WINDOW_CLOSED or event_manage == "Exit":
                    break
                elif event_manage == "Back":
                    manage_window.close()
                    window.un_hide()
                    break

            manage_window.close()


        elif event == "-PC_USERS-":

            window.hide()

            manage_pc_layout = create_manage_pc_users_layout()

            manage_pc_window = sg.Window("Manage PC Users", manage_pc_layout)

            current_student = None  # Initialize current_student outside the loop

            while True:

                event_pc, values_pc = manage_pc_window.read()

                if event_pc == sg.WINDOW_CLOSED or event_pc == "Back":

                    manage_pc_window.close()

                    window.un_hide()

                    break


                elif event_pc == "Search":

                    search_term = values_pc['search_field'].strip().lower()

                    search_criteria = values_pc['search_criteria']

                    student_match = None

                    if search_criteria == 'Student Number':

                        student_match = next(

                            (student for student in student_data

                             if str(student['User Number']) == search_term),

                            None

                        )


                    elif search_criteria == 'Student Name':

                        student_match = next(

                            (student for student in student_data

                             if student['User Name'].strip().lower() == search_term),

                            None

                        )

                    if student_match:

                        current_student = student_match  # Update current_student

                        manage_pc_window['student_display'].update(

                            value=f"{student_match['User Name']}, {student_match['User Number']}, {student_match['Course']}"

                        )


                    else:

                        # Show an error with a button to register a new user

                        result = sg.popup_yes_no(

                            "User not found. Would you like to register a new user?",

                            title="Error"

                        )

                        if result == "Yes":

                            # Close the current window and open the registration window

                            manage_pc_window.close()

                            registration_layout = create_register_student_layout()

                            registration_window = sg.Window("Register User", registration_layout)

                            while True:

                                event_reg, values_reg = registration_window.read()

                                if event_reg == sg.WINDOW_CLOSED or event_reg == "Cancel":

                                    break

                                elif event_reg == "Save":

                                    if validate_input(values_reg):

                                        existing_data = pd.read_excel('users_data.xlsx', dtype={'User Number': str})

                                        if values_reg['student_number'] in existing_data['User Number'].values:

                                            sg.popup_error(

                                                f"User with User Number {values_reg['student_number']} already exists. Please enter a different User Number.")


                                        else:

                                            student_data.append({

                                                'User Name': values_reg['student_name'],

                                                'User Number': values_reg['student_number'],

                                                'Course': values_reg['course']

                                            })

                                            save_student_data(student_data[-1])

                                            sg.popup("User registered successfully!")

                                            break  # Break out of the registration loop

                            registration_window.close()

                            # Re-open the Manage PC Users window

                            manage_pc_window = sg.Window("Manage PC Users", create_manage_pc_users_layout())


                elif event_pc == "Current Time In":

                    current_time = datetime.datetime.now().strftime("%I:%M %p")

                    manage_pc_window['time_in_hour'].update(current_time.split(':')[0])

                    manage_pc_window['time_in_minute'].update(current_time.split(':')[1].split()[0])

                    manage_pc_window['time_in_am_pm'].update(current_time.split()[1])


                elif event_pc == "Time Out":

                    current_time = datetime.datetime.now() + datetime.timedelta(hours=1)

                    manage_pc_window['time_out_hour'].update(current_time.strftime("%I"))

                    manage_pc_window['time_out_minute'].update(current_time.strftime("%M"))

                    manage_pc_window['time_out_am_pm'].update(current_time.strftime("%p"))


                elif event_pc == "Approve":

                    if current_student is None:

                        sg.popup_error("Please search for a User first.")

                    elif values_pc['pc_number'] == '' or values_pc['assigned_staff'] == '':

                        sg.popup_error(

                            "PC Number and Assigned Staff are required fields. Please fill in the required information.")

                    elif all(value != '' for key, value in values_pc.items() if

                             key in ['student_name', 'student_number', 'course']):

                        if current_student:

                            try:

                                # Read the existing user logs data

                                user_logs_df = pd.read_excel('user_logs.xlsx', dtype={'PC Number': str})

                                # Check if the PC number is occupied

                                pc_occupied = user_logs_df['PC Number'].astype(str).eq(values_pc['pc_number']).any()


                            except FileNotFoundError:

                                # File not found, assume no PC numbers are occupied

                                pc_occupied = False

                            if pc_occupied:

                                sg.popup_error(f"PC Number {values_pc['pc_number']} is already occupied.")

                            else:

                                pc_entry = {

                                    'PC Number': values_pc['pc_number'],

                                    'Search Field': values_pc['search_field'],

                                    'User Name': current_student['User Name'],

                                    'User Number': current_student['User Number'],

                                    'Course': current_student['Course'],

                                    'Date': f"{values_pc['month']}/{values_pc['day']}/{values_pc['year']}",

                                    'Time In': f"{values_pc['time_in_hour']}:{values_pc['time_in_minute']} {values_pc['time_in_am_pm']}",

                                    'Time Out': f"{values_pc['time_out_hour']}:{values_pc['time_out_minute']} {values_pc['time_out_am_pm']}",

                                    'Assigned Staff': values_pc['assigned_staff']

                                }

                                # Save data to both logs

                                save_pc_user_data(pc_entry)

                                save_user_logs_data(pc_entry)

                                sg.popup("PC user data saved successfully!")

                        else:

                            sg.popup_error("User not found. Please search for a valid User.")

                    else:

                        sg.popup_error(

                            "One or more required fields are blank. Please fill in the required information.")

            manage_pc_window.close()



        elif event == "-MANAGE_USER_LOGS-":

            window.hide()

            manage_user_logs_layout = create_manage_user_logs_layout()

            manage_user_logs_window = sg.Window("Manage User Logs", manage_user_logs_layout, finalize=True)

            while True:

                event_manage_logs, values_manage_logs = manage_user_logs_window.read()

                if event_manage_logs == sg.WINDOW_CLOSED or event_manage_logs == "Back":

                    manage_user_logs_window.close()

                    window.un_hide()

                    break


                elif event_manage_logs == "-DELETE_ROW-":

                    selected_row = values_manage_logs['user_logs_table']

                    if selected_row:

                        try:

                            user_logs_df = pd.read_excel('user_logs.xlsx', dtype={'PC Number': str})

                            user_logs_df = user_logs_df.drop(selected_row[0]).reset_index(drop=True)

                            user_logs_df.to_excel('user_logs.xlsx', index=False)

                            sg.popup("Row deleted successfully!")

                            user_logs_data = user_logs_df.values.tolist()

                            manage_user_logs_window['user_logs_table'].update(values=user_logs_data)

                        except FileNotFoundError:

                            sg.popup_error("No user logs file found.")

                    else:

                        sg.popup_error("Please select a row to delete.")

            manage_user_logs_window.close()

            window.un_hide()

    window.close()


if __name__ == "__main__":
    main()
