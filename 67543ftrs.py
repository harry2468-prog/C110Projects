import tkinter as tk

# Global state
current_step = 'start'
valid_choices = ()

def update_prompt(text, choices):
    global valid_choices
    prompt.delete(0, tk.END)
    prompt.insert(0, '')
    label_prompt.config(text=text)
    valid_choices = choices




def get_action():
    global current_step
    response = prompt.get().strip().lower()

    if response not in valid_choices:
        label_response.config(text=f'Invalid input: "{response}", Please enter one of: {", ".join(valid_choices)}.')
        return

    label_response.config(text=f'You chose: {response}')

    if current_step == 'start':
        if response == 'explore narrow tunnel':
            label_response1.config(text='You decide to explore the mine further.')
            label_response2.config(text='You hear a faint dripping sound.')
            label_response3.config(text='You find stainless steel pillars with bolts.')
            label_response4.config(text='You estimate the forces acting on them.In addition,you find a random sample of the ore for collection')
            update_prompt('What do you want to do? (collect/continue):', ('collect', 'continue'))
            current_step = 'tunnel_choice'

        elif response == 'enter mining equipment room':
            label_response1.config(text='You enter the room: old mining tools and logs.')
            update_prompt('What do you want to do?(open logs/leave):',('open logs','leave'))
            current_step = 'logs'
        elif response == 'enter substation room':
            label_response1.config(text='You see old electrical equipment.')
            update_prompt('What do you want to do?(explore the equipment/leave):',('explore the equipment','leave'))
            current_step = 'explore'
        else:
            label_response1.config(text='You decide to leave the mine safely.')

    elif current_step == 'tunnel_choice':
        if response == 'collect':
            label_action1.config(text='You collect glowing crystals.')
            label_action2.config(text='They might be valuable!')
            update_prompt('What do you want to do?(analyze sample/leave):',('analyze sample','leave'))
            current_step = 'analyze'
        else:
            label_action1.config(text='You leave the crystals and go deeper.')
            label_action2.config(text='You find a large cavern with mining carts.')
            update_prompt('There are lifts and steps designed to go underground of the mine(proceed with steps underground/leave):',('proceed with steps underground','leave'))
            current_step = 'lifts'
    elif current_step == 'analyze':
        if response == 'analyze sample':
            label_action1.config(text = 'Switch on the XRF and insert the crystals inside the lid')
            label_action2.config(text = 'The LCD of the XRF displays proportions of Fe,Cu,Al,Pb,Sn,Ni,Au,Ag,(C6H10O3)n,Na2O.CaO.6SiO2,(C6H5OH.CH2)n,(C22H10N2O5)n,(C2H4)n and SiO2')
            update_prompt('Do you want the proportion as a percentage or a fraction(percentage/fraction):',('percentage','fraction'))
            current_step = 'proportion'       
        else:
            label_action1.config(text = 'You are out of the tunnel') 
    elif current_step == 'lifts':
        if response == 'proceed with steps underground':
            label_action1.config(text = 'Measure the angle of the elevation and depression of the steps') 
            update_prompt('Is the angle of depression greater or less than an acute angle?(greater than an acute angle/less than an acute angle):',('greater than an acute angle','less than an acute angle'))
            current_step = 'angle'
        else:
            label_action1.config(text = 'You are walking out of the narrow tunnel') 
    elif current_step == 'angle':
        if response == 'greater than an acute angle':
            label_action1.config(text = 'The steps have a steeper gradient hence require less pre-caution') 
            update_prompt('What is the type of material used to construct the steps?(iron/concrete/wood):',('iron','concrete','wood'))
            current_step = 'material'
        else:
            label_action1.config(text = 'The slope of the steps are less steep and require careful pre-caution')
    elif current_step == 'material':
        if response == 'iron':
            label_action1.config(text = 'Please note that steel corrodes at a specific rate hence be cautious!')
            update_prompt('What is the type of steel used to construct the steps(galvanized iron/stainless steel/wrought iron):',('galvanized iron','stainless steel','wrought iron'))
            current_step = 'used'
        elif response == 'concrete':
            label_action1.config(text = 'Please note that since the steps also causes forces on the mine proceed with caution!')
        else:
            label_action1.config(text = 'The wood has potential to collapse')
    elif current_step == 'used':
        if response == 'galvanized iron':
            label_action1.config(text = 'The steps have corroded considering that the mine started 100 years ago and the corrosion rate of iron')
        elif response == 'stainless steel':
            label_action1.config(text = 'The steps have potential of having strength but proceed with caution!')
        else:
            label_action1.config(text =' The steps have already collapsed considering the number of years of the mine in operation')                                                        
    elif current_step == 'proportion':
        if response == 'percentage':
            label_action1.config(text = 'Display the proportion of the crystal as a percentage')
            update_prompt('Send the proportion fraction to the Process Engineer?(harry/chackspear):',('harry','chackspear'))
            current_step = 'processing'        
        else:
            label_action1.config(text = 'Display the proportion in fraction')
    elif current_step == 'processing':
        if response == 'harry':
            label_action1.config(text = 'Please contact Engineer Harry with his details or visit him to his office')
            update_prompt('Contact Engineer Harry or Visit Engineer Harry?(contact engineer harry/visit engineer harry):',('contact engineer harry','visit engineer harry'))
            current_step = 'harry'
        else:
            label_action1.config(text = 'Please contact Engineer Chackspear with his details or visit him to his office')
            update_prompt('Contact Engineer Chackspear or Visit Engineer Chackspear?(contact engineer chackspear/visit engineer chackspear):',('contact engineer chackspear','visit engineer chackspear'))
            current_step = 'chackspear'
    elif current_step == 'chackspear':
        if response == 'chackspear':
            label_action1.config(text = 'Please note Engineer Chackspear is currently unavailable.He is currently in Beijing attending the World Congress of Chemical Engineers')
            label_action2.config(text = 'Engineer Chackspear can be reached within a forty-night.Thank you for your patience!')
        else:
            label_action1.config(text = 'Please note that Engineer Chackspear is currently unavailable.He is currently in Cape Town at Enlit Africa attending a business conference')
            label_action2.config(text = 'Engineer Chackspear can be reached within a month.Thank you for your patience!')            
    elif current_step == 'harry':
        if response == 'contact engineer harry':
            label_action1.config(text = 'Please note that Engineer Harry can be contacted via email or whatsapp')
            update_prompt('How do you want to contact Engineer Harry?(email/whatsapp):',('email','whatsapp'))
            current_step = 'want'
        else:
            label_action1.config(text = 'You walk out of the mine and drive to Engineer Harry office')
    elif current_step == 'want':
        if response == 'email':
            label_action1.config(text ='You need the mail address of Engineer Harry')
            update_prompt('Please enter the mail address of Engineer Harry?(harry@relithia.com/harry@relithiaenergy.com):',('harry@relithia.com','harry@relithiaenergy.com'))
            current_step = 'mail' 
        else:
            label_action1.config(text ='You need Engineer Harry whatsapp number to reach him?(263783393296/13568654356):')
            update_prompt('Please enter the whatsapp number of Engineer Harry?(263783393296/13568654356)',('263783393296','13568654356'))
            current_step = 'number'  
    elif current_step == 'mail':
        if response == 'harry@relithia.com':
            label_action1.config(text ='Hello Mining Engineer,How are you doing today.At Relithia Energy we offer consulting services such as designing at a cost')
            label_action2.config(text ='Our costs range from US$10000 for designing mass balances and US$20000 for designing both mass and energy balances')
            update_prompt('Which design do you want?(mass balance design/energy balance design):',('mass balance design','energy balance design'))
            current_step = 'balance'
        else:
            label_action1.config(text ='Hello Mining Engineer,How are you doing today.At Relithia Energy we offer consulting services such as designing at a cost')
            label_action2.config(text ='Our costs range from US$10000 for designing mass balances and US$20000 for designing both mass and energy balances')
            update_prompt('Which design do you want?(mass balance design/energy balance design):',('mass balance design','energy balance design'))
            current_step = 'balance'
    elif current_step == 'number':
        if response == '263783393296':
            label_action1.config(text = 'Hello Mining Engineer,How are you doing today.At Relithia Energy we offer consulting services such as designing at a cost')
            label_action2.config(text ='Our costs range from US$10000 for designing mass balances and US$20000 for designing both mass and energy balances')
            update_prompt('Which design do you want?(mass balance design/energy balance design):',('mass balance design','energy balance design'))
            current_step = 'balance'
        else:
            label_action1.config(text = 'Hello Mining Engineer,How are you doing today.At Relithia Energy we offer consulting services such as designing at a cost')
            label_action2.config(text ='Our costs range from US$10000 for designing mass balances and US$20000 for designing both mass and energy balances')
            update_prompt('Which design do you want?(mass balance design/energy balance design):',('mass balance design','energy balance design'))
            current_step = 'balance'    
    elif current_step == 'balance':
        if response == 'mass balance design':
            label_action1.config(text ='In order to complete the technical process design of the plant,you have to pay US$10000')
            update_prompt('Complete the payment process?(pay $10000/never pay):',('pay $10000','never pay'))
            current_step = 'payment'
        else:
            label_action1.config(text ='In order to complete the technical process design of the plant,you have to pay US$20000')
            update_prompt('Complete the payment process?(pay $20000/never pay):',('pay $20000','never pay'))
            current_step = 'complete'
    elif current_step == 'payment':
        if response == 'pay $10000':
            label_action1.config(text ='In order to complete the technical process design of the plant,you have to pay US$10000')
            update_prompt('Which platform do you want to processing transanction?(visa/mastercard):',('visa','mastercard'))
            current_step = 'platform'
        else:
            label_action1.config(text = 'Please visit Relithia when you have sifficient funds')    
    elif current_step == 'complete':
        if response == 'pay $20000':
            label_action1.config(text ='In order to complete the technical process design of the plant,you have to pay US$20000')
            update_prompt('Which platform do you want to processing transanction?(visa/mastercard):',('visa','mastercard'))
            current_step = 'platform'
        else:
            label_action1.config(text ='Please visit Relithia Energy when you have sufficient funds')
    elif current_step == 'platform':
        if response == 'visa':
            label_action1.config(text = 'You need Relithia Energy Visa account to perform transaction')
            update_prompt('Complete transaction(pay $10000/pay $20000):',('pay $10000','pay $20000'))
            current_step = 'transaction'
        else:
            label_action1.config(text = 'You need Relithia Energy Mastercard account to perform transaction')
            update_prompt('Complete transaction(pay $10000/pay $20000):',('pay $10000','pay $20000'))
            current_step = 'pay'
    elif current_step == 'transaction':
        if response == 'pay $10000':
            label_action1.config(text = 'You need the account number')
            update_prompt('Enter the account number(10076543213456/322145679985):',('10076543213456','322145679985'))
            current_step = 'the'
        else:
            label_action1.config(text = 'You need the account number')
            update_prompt('Enter the account number(789076543225/987654325798):',('789076543225','987654325798'))
            current_step = 'enter'

    elif current_step == 'the':
        if response == '10076543213456':
            label_action1.config(text = 'Payment made successfully')
            label_action2.config(text = 'Please you have to enter the percentage of the proportion of minerals')
            update_prompt('Do you require a digital simulation design or a printed copy?(digital design/printed copy):',('digital design','printed copy'))
            current_step = 'require'
        elif response == '322145679985':
            label_action1.config(text = 'Payment made sucessfully') 
            label_action2.config(text = 'Please you have to enter the percentage of the proportion of minerals')
            update_prompt('Do you require a digital simulation design or a printed copy?(digital design/printed copy):',('digital design','printed copy'))
            current_step = 'require' 
        else:
            label_action1.config(text = 'Insufficient funds') 
    elif current_step == 'enter':
        if response == '789076543225':
            label_action1.config(text = 'Payment made successfully')
            label_action2.config(text = 'Please you have to enter the percentage of the proportion of minerals')
            update_prompt('Do you require a digital simulation design or a printed copy?(digital design/printed copy):',('digital design','printed copy'))
            current_step = 'require'
        elif response == '987654325798':
            label_action1.config(text = 'Payment made successfully')
            label_action2.config(text = 'Please you have to enter the percentage of the proportion of minerals')
            update_prompt('Do you require a digital simulation design or a printed copy?(digital design/printed copy):',('digital design','printed copy'))
            current_step = 'require'   
    elif current_step == 'logs':
        if response == 'open logs':
            label_action1.config(text = 'You flip through old journals, learning the mine history and hazards.The mine was closed due to safety concerns and declining mineral reserves')
            label_action2.config(text = 'You discover a hidden shaft that might contain valuable minerals.') 
            update_prompt('What do you want to do?(design the mine/leave):',('design the mine','leave'))
            current_step = 'design'
        else:
            label_action1.config(text = 'You are out of the room')       
            update_prompt('What do you want to do?(design the mine/leave):',('design the mine','leave'))
    elif current_step == 'explore':
        if response == 'explore the equipment':
            label_action1.config(text ='You inspect coils of copper and aluminum and see exposed wiring.')
            update_prompt('Open toolbox to dismantle electrical equipment or leave? (dismantle/leave):', ('dismantle','leave'))
            current_step = 'toolbox'
        else:
            label_action1.config(text = 'You are out the electrical room')
    elif current_step == 'toolbox':
        if response  == 'dismantle':
            label_action1.config(text = 'You dismantle some components—bolts, nuts, and wires are disconnected')
        else:
            label_action1.config(text = 'You are out of the electrical room')  
    elif current_step == 'design':
        if response =='design the mine':
            label_action1.config(text ='You open your simulation software and map the mine using journal parameters.') 
            update_prompt('What material is used to construct the pillars?(wood/concrete/steel):',('wood','concrete','steel'))
            current_step = 'pillars'     
    elif current_step =='pillars':
        if response =='wood':
            label_action1.config(text ='The mine pillars has potential to collapse considering the forces of the mine assuming that wooden pillars were constructed 100 years ago')
        elif response =='concrete':
            label_action1.config(text = 'The pillars has strength considering the compressional forces and weight of the mine')
        else:
            label_action1.config(text ='Please check the type of steel used for pillars to determine the corrosive rate used to determine strength of the pillars')
            update_prompt('What is the type of steel used to construct the pillars?(galvanized steel/stainless steel/wrought iron)',('galvanized steel','stainless steel','wrought iron'))         
            current_step = 'steel'   
    elif current_step == 'steel':
        if response == 'galvanized steel':
            label_action1.config(text = 'The pillars have corroded and the mine has potential to collapse because of the corrosion rate of galvanized iron for 100 years')
        elif response == 'stainless steel':
            label_action1.config(text = 'The mine pillars have strength but inspecting the tunnel requires diligence')
        else:
            label_action1.config(text = 'Some sections of the mine have already collapsed because of the corrosion rate of wrought iron for 100 years')
    elif current_step == 'require':
        if response == 'printed copy':
            label_action1.config('The printed copy of the design is to be delivered to your address within two working days')
            label_action2.config('Thank you for visiting Relithia Energy!') 
        else:
            try:
                label_action1.config(text ='Inorder to complete the design,the proportion of materials displayed in XRF must be entered')
                label_design1.config(text = 'Constituent')
                label_design2.config(text = 'Fe')
                label_design3.config(text = 'Cu')
                label_design4.config(text = 'Al')
                label_design5.config(text = 'Pb')
                label_design6.config(text = 'Sn')
                label_design7.config(text = 'Ni')
                label_design8.config(text = 'Au')
                label_design9.config(text = 'Ag')
                label_design10.config(text = '(C6H10O3)n')
                label_design11.config(text = 'Na2O.CaO.6SiO2')
                label_design12.config(text = '(C6H5OH.CH2)n')
                label_design13.config(text = '(C22H10N2O5)n')
                label_design14.config(text = '(C2H4)n')
                label_design15.config(text = 'SiO2')
                label_total.config(text = 'Total mass')
                label_design16.config(text = 'Mass')
                Iron = float(entry_iron.get())
                Copper = float(entry_copper.get())
                Aluminum = float(entry_aluminum.get())
                Lead = float(entry_lead.get())
                Tin = float(entry_tin.get())
                Nickel = float(entry_nickel.get())
                Gold = float(entry_gold.get())
                Silver = float(entry_silver.get())
                Epoxide_resin = float(entry_epoxide.get())
                Fiberglass = float(entry_fiberglass.get())
                Phenolic = float(entry_phenolic.get())
                Polyamide = float(entry_polyamide.get())
                Polyethene = float(entry_polyethene.get())
                Silicon_dioxide = float(entry_silicon.get())
                Total_mass = Iron + Copper + Aluminum + Lead + Tin + Nickel + Gold + Silver + Epoxide_resin + Fiberglass + Phenolic + Polyamide + Polyethene + Silicon_dioxide
                Metal_proportion = (Iron + Copper + Aluminum + Lead + Tin + Nickel + Gold + Silver)/(Iron + Copper + Aluminum + Lead + Tin + Nickel + Gold + Silver + Epoxide_resin + Fiberglass + Phenolic + Polyamide + Polyethene + Silicon_dioxide)
                label_Total_mass.config(text =f'{Total_mass}')
                label_Metal_proportion1.config(text =f'The metals proportion is {Metal_proportion}')
                label_Metal_proportion2.config(text = 'According to the structural characteristics of the crystals,the following process is implemented with a capacity 300kg/hr.')
                Vibrating_Feeder = 3*Total_mass
                Conveyor_belt1 = Vibrating_Feeder
                Shredder = Conveyor_belt1
                Conveyor_belt2 = Shredder
                crusher = Conveyor_belt2
                Conveyor_belt3 = crusher
                Airflow_Separator = Conveyor_belt3
                Pipe1 = 0.15*Airflow_Separator
                Pipe2 = 0.2532*Airflow_Separator
                Electrostatic_Separator = Pipe2
                Pipe3 = 3*Electrostatic_Separator
                Conveyor_belt4 = (1-0.2532)*Airflow_Separator
                Grinder = Conveyor_belt4
                Pipe4 = 0.009*Grinder
                Magnetic_Separator = Pipe4
                Conveyor_belt5 = (1-0.009)*Grinder
                Dense_Media = Conveyor_belt5
                Conveyor_belt6 = 0.9159*Dense_Media
                Pipe5 = 3*Conveyor_belt6
                Gravity_Separator = Conveyor_belt6
                Conveyor_belt7 = 0.994*Gravity_Separator
                Spiral_Concentrator = Conveyor_belt7
                Power1 = 0.0037*Vibrating_Feeder
                Power2 = 0.0027*Conveyor_belt1
                Power3 = 0.0045*Shredder
                Power4 = 0.006*Conveyor_belt2
                Power5 = 0.08*crusher
                Power6 = 0.09*Conveyor_belt3
                Power7 = 0.06*Airflow_Separator
                Power8 = 0.075*Pipe1
                Power9 = 0.043*Pipe2
                Power10 = 0.278*Electrostatic_Separator
                Power11 = 0.09*Pipe3
                Power12 = 0.14*Conveyor_belt4
                Power13 = 0.075*Grinder
                Power14 = 0.0876*Pipe4
                Power15 = 0.098*Magnetic_Separator
                Power16 = 0.054*Conveyor_belt4
                Power17 = 0.087*Dense_Media
                Power18 = 0.0654*Conveyor_belt6
                Power19 = 0.09876*Pipe5
                Power20 = 0.0345*Gravity_Separator
                Power21 = 0.09876*Conveyor_belt7
                Power22 = 0.0987*Spiral_Concentrator
                # Create table layout for displaying a digital simulation design
                # Frame to hold the table (same grid position as the old shapes)
                # Frame to hold the empty table
                table_frame = tk.Frame(root, bg='white', relief=tk.RIDGE, bd=2)
                table_frame.grid(row=2, column=4, columnspan=3, padx=5, pady=5)
                table_frame.tkraise()

                # Create a 23x3 table of StringVars
                table_data = [[tk.StringVar() for _ in range(3)] for _ in range(23)]
                try:
                    equipment_info = [
                                      ("Equipment", "Capacity", "Power"),
                                      ("Vibrating Feeder", f"{Vibrating_Feeder}", f"{Power1}"),
                                      ("Conveyor belt 1", f"{Conveyor_belt1}", f"{Power2}"),
                                      ("Shredder", f"{Shredder}", f"{Power3}"),
                                      ("Conveyor belt 2", f"{Conveyor_belt2}", f"{Power4}"),
                                      ("Hummer crusher", f"{crusher}", f"{Power5}"),
                                      ("Conveyor belt 3", f"{Conveyor_belt3}", f"{Power6}"),
                                      ("Airflow Separator", f"{Airflow_Separator}", f"{Power7}"),
                                      ("Pipe 1", f"{Pipe1}", f"{Power8}"),
                                      ("Pipe 2", f"{Pipe2}", f"{Power9}"),
                                      ("Electrostatic Separator", f"{Electrostatic_Separator}", f"{Power10}"),
                                      ("Pipe 3", f"{Pipe3}", f"{Power11}"),
                                      ("Conveyor 4", f"{Conveyor_belt4}", f"{Power12}"),
                                      ("Grinding mill", f"{Grinder}", f"{Power13}"),
                                      ("Pipe 4", f"{Pipe4}", f"{Power14}"),
                                      ("Magnetic Seperator", f"{Magnetic_Separator}", f"{Power15}"),
                                      ("Conveyor belt 5", f"{Conveyor_belt5}", f"{Power16}"),
                                      ("Dense Medium Separator", f"{Dense_Media}", f"{Power17}"),
                                      ("Conveyor belt 6", f"{Conveyor_belt6}", f"{Power18}"),
                                      ("Pipe 5", f"{Pipe5}", f"{Power19}"),
                                      ("Gravity Separator", f"{Gravity_Separator}", f"{Power20}"),
                                      ("Conveyor belt 7", f"{Conveyor_belt7}", f"{Power21}"),
                                      ("Spiral Collector", f"{Spiral_Concentrator}", f"{Power22}"),
                                       ]
                    for i, (Equipment, Capacity, Power) in enumerate(equipment_info):
                        table_data[i][0].set(Equipment)
                        table_data[i][1].set(Capacity)
                        table_data[i][2].set(Power)
                        tk.Label(table_frame, text=Equipment, bg='brown', width=15, height=1, relief=tk.GROOVE).grid(row=i, column=0, padx=2, pady=2)
                        tk.Label(table_frame, text=Capacity, bg='brown', width=15, height=1, relief=tk.GROOVE).grid(row=i, column=1, padx=2, pady=2)
                        tk.Label(table_frame, text=Power, bg='brown', width=15, height=1, relief=tk.GROOVE).grid(row=i, column=2, padx=2, pady=2)
                except Exception as e:
                    print("Error building table:", e)

            except ValueError:
                label_Total_mass.config(text = f'Error:Please enter valid numerical values')


# GUI setup
root = tk.Tk()
root.title('Mine Adventure')
root.config(background='lightgreen')



# Labels
label_Mining_Engineer = tk.Label(root, text='You are a Mining Engineer specializing in abandoned mine exploration.')
label_Mining_Engineer.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

label_hired = tk.Label(root, text='You have been hired to assess the Oakwood Mine which started operations 100 years ago.')
label_hired.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

label_prompt = tk.Label(root, text='What do you want to do? (explore narrow tunnel/enter mining equipment room/enter substation room/leave):')
label_prompt.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

prompt = tk.Entry(root, width=50)
prompt.grid(row=3, column=0, padx=5, pady=5)

button_response = tk.Button(root, text='Next', command=get_action)
button_response.grid(row=3, column=1, padx=5, pady=5)

label_response = tk.Label(root, text='')
label_response.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

label_response1 = tk.Label(root, text='')
label_response1.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

label_response2 = tk.Label(root, text='')
label_response2.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

label_response3 = tk.Label(root, text='')
label_response3.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

label_response4 = tk.Label(root, text='')
label_response4.grid(row=8, column=0, columnspan=2, padx=5, pady=5)

label_action1 = tk.Label(root, text='')
label_action1.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

label_action2 = tk.Label(root, text='')
label_action2.grid(row=10, column=0, columnspan=2, padx=5, pady=5)

label_design1 =tk.Label(root,text = '')
label_design1.grid(row =0,column = 2,padx =5,pady =5)

label_design2 = tk.Label(root,text ='')
label_design2.grid(row =1,column = 2 ,padx =5,pady =5)

label_design3 = tk.Label(root,text = '')
label_design3.grid(row =2,column =2,padx =5,pady =5)

label_design4 = tk.Label(root,text = '')
label_design4.grid(row = 3,column = 2,padx =5,pady =5)

label_design5 = tk.Label(root,text = '')
label_design5.grid(row =4,column =2,padx =5,pady =5)

label_design6 = tk.Label(root,text = '')
label_design6.grid(row =5,column =2,padx =5,pady =5)

label_design7 = tk.Label(root,text = '')
label_design7.grid(row = 6,column = 2,padx =5,pady =5)

label_design8 = tk.Label(root,text ='')
label_design8.grid(row =7,column = 2,padx =5,pady =5)

label_design9 = tk.Label(root,text ='')
label_design9.grid(row = 8,column =2,padx =5,pady =5)

label_design10 = tk.Label(root,text = '')
label_design10.grid(row = 9,column = 2,padx =5,pady =5)

label_design11 = tk.Label(root,text ='')
label_design11.grid(row = 10,column = 2,padx =5,pady =5)

label_design12 = tk.Label(root,text ='')
label_design12.grid(row = 11,column = 2,padx =5,pady =5)


label_design13 = tk.Label(root,text ='')
label_design13.grid(row = 12,column = 2,padx =5,pady =5)

label_design14 = tk.Label(root,text = '')
label_design14.grid(row =13,column =2,padx =5,pady =5)

label_design15 = tk.Label(root,text ='')
label_design15.grid(row = 14,column = 2,padx =5,pady =5)

label_total = tk.Label(root,text ='')
label_total.grid(row = 15,column =2,padx =5,pady =5 )

label_design16 = tk.Label(root,text = '')
label_design16.grid(row =0,column = 3,padx =5,pady =5)

entry_iron = tk.Entry(root,width =5)
entry_iron.grid(row =1,column = 3,padx =5,pady =5)

entry_copper = tk.Entry(root,width =5)
entry_copper.grid(row =2,column = 3,padx =5,pady =5)

entry_aluminum = tk.Entry(root,width =5)
entry_aluminum.grid(row =3,column = 3,padx =5,pady =5)


entry_lead = tk.Entry(root,width =5)
entry_lead.grid(row =4,column =3,padx =5,pady =5)


entry_tin = tk.Entry(root,width =5)
entry_tin.grid(row =5,column = 3,padx =5,pady =5)

entry_nickel = tk.Entry(root,width =5)
entry_nickel.grid(row =6,column = 3,padx =5,pady =5)

entry_gold = tk.Entry(root,width =5)
entry_gold.grid(row = 7,column = 3,padx =5,pady =5)

entry_silver = tk.Entry(root,width =5)
entry_silver.grid(row =8,column =3,padx =5,pady =5)

entry_epoxide = tk.Entry(root,width =5)
entry_epoxide.grid(row =9,column =3,padx =5,pady =5)

entry_fiberglass = tk.Entry(root,width =5)
entry_fiberglass.grid(row = 10,column =3,padx =5,pady =5)

entry_phenolic = tk.Entry(root,width =5)
entry_phenolic.grid(row =11,column =3,padx =5,pady =5)

entry_polyamide = tk.Entry(root,width =5)
entry_polyamide.grid(row = 12,column =3,padx =5,pady =5)


entry_polyethene = tk.Entry(root,width =5)
entry_polyethene.grid(row = 13,column = 3,padx =5,pady =5)


entry_silicon = tk.Entry(root,width =5)
entry_silicon.grid(row = 14,column =3,padx =5,pady =5)

button_Total_mass = tk.Button(root,text ='Total mass',command = get_action)
button_Total_mass.grid(row =15,column = 2,padx =5,pady =5)


label_Total_mass = tk.Label(root,text ='')
label_Total_mass.grid(row =15,column = 3,padx =5,pady =5)

label_Metal_proportion1 = tk.Label(text ='')
label_Metal_proportion1.grid(row =0,column =4,padx =5,pady =5)

label_Metal_proportion2 = tk.Label(text ='')
label_Metal_proportion2.grid(row =1,column =4,padx =5,pady =5)



# Initialize prompt
update_prompt(
    'What do you want to do? (explore narrow tunnel/enter mining equipment room/enter substation room/leave):',
    ('explore narrow tunnel', 'enter mining equipment room', 'enter substation room', 'leave')
)

root.mainloop()
