import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import matplotlib.pyplot as plt
import numpy as np
import random

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
                label_Total_mass.config(text =f'{Total_mass}')
                try:
                    #  Crystals on conveyor
                    crystal_positions = [0, 4, 8]

                    #Air particles on pipe
                    Air_particles = [0, 2, 4, 6, 8]

                    #Organic particles on pipe
                    Organic_particles =[0,2,4,6,8]

                    
                    #Electron flow
                    Electron =[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
                    
                    def draw_trapezoid(ax, x, y, z, dx, dy, dz, color='gray', alpha=0.9):
                        shrink = 0.2
                        # Bottom face
                    def draw_trapezoid(ax, x, y, z, dx, dy, dz, color='gray', alpha=0.9):
                        shrink = 0.2
                        # Bottom face
                        p0 = [x, y, z]
                        p1 = [x + dx, y, z]
                        p2 = [x + dx, y + dy, z]
                        p3 = [x, y + dy, z]
                        # Top face (shrunk)
                        p4 = [x + shrink, y + shrink, z + dz]
                        p5 = [x + dx - shrink, y + shrink, z + dz]
                        p6 = [x + dx - shrink, y + dy - shrink, z + dz]
                        p7 = [x + shrink, y + dy - shrink, z + dz]

                        vertices = [
                            [p0, p1, p2, p3],  # bottom
                            [p4, p5, p6, p7],  # top
                            [p0, p1, p5, p4],  # front
                            [p1, p2, p6, p5],  # right
                            [p2, p3, p7, p6],  # back
                            [p3, p0, p4, p7]   # left
                            ]
                        ax.add_collection3d(Poly3DCollection(vertices, facecolors=color, linewidths=1, edgecolors='black', alpha=alpha))

                    def draw_trapezoid_upside_down(ax, x, y, z, dx, dy, dz, color='gray', alpha=0.9):
                        shrink = 0.2  # Top face (larger base)
                        p0 = [x, y, z + dz]
                        p1 = [x + dx, y, z + dz]
                        p2 = [x + dx, y + dy, z + dz]
                        p3 = [x, y + dy, z + dz]

                        # Bottom face (smaller base)
                        p4 = [x + shrink, y + shrink, z]
                        p5 = [x + dx - shrink, y + shrink, z]
                        p6 = [x + dx - shrink, y + dy - shrink, z]
                        p7 = [x + shrink, y + dy - shrink, z]

                        vertices = [
                            [p0, p1, p2, p3],  # top
                            [p4, p5, p6, p7],  # bottom
                            [p0, p1, p5, p4],  # front
                            [p1, p2, p6, p5],  # right
                            [p2,p3, p7, p6],  # back
                            [p3, p0, p4, p7]  # left
                            ]

                        ax.add_collection3d(Poly3DCollection(vertices, facecolors=color, linewidths=1, edgecolors='black', alpha=alpha))


                    def draw_plant(ax):
                        ax.clear()
                        ax.set_title("Digital design simulation")
                        ax.set_xlim([-10, 40])
                        ax.set_ylim([-20, 10])
                        ax.set_zlim([0, 10])
                        ax.set_xlabel("Length")
                        ax.set_ylabel("Width")
                        ax.set_zlabel("Height")


                        def draw_cone_upside_down(ax, x, y, z, height, radius, color='gray'):
                            u = np.linspace(0, 2 * np.pi, 100)
                            v = np.linspace(0, height, 100)
                            u, v = np.meshgrid(u, v)
                            x_cone = x + (1 -v / height) * radius * np.cos(u)
                            y_cone = y + (1 -v / height) * radius * np.sin(u)
                            z_cone = z + v
                            ax.plot_surface(x_cone, y_cone, z_cone, color=color, alpha=0.9)
                        
                        def create_cylinder(x,y,z,height,radius,color,ax):
                            #Create a cylinder
                            z_cylinder = np.linspace(0,height,100)
                            theta = np.linspace(0,2*np.pi,100)
                            theta_grid,z_grid = np.meshgrid(theta,z_cylinder)
                            x_grid = radius*np.cos(theta_grid)+ x
                            y_grid = radius*np.sin(theta_grid)+ y
                            ax.plot_surface(x_grid,y_grid,z_grid+z,color=color,alpha = 0.9)

                        def draw_triangular_prism(ax, base_center, width, depth, height, color='grey', alpha=1.0):
                            x, y, z = base_center
                            w, d, h = width / 2, depth / 2, height

                            vertices = [
                                [x - w, y - d, z],
                                [x + w, y - d, z],
                                [x + w, y + d, z],
                                [x -w, y + d, z],
                                [x, y, z -h],
                                ]

                            faces = [
                                [vertices[0], vertices[1], vertices[4]],
                                [vertices[1], vertices[2], vertices[4]],
                                [vertices[2], vertices[3], vertices[4]],
                                [vertices[3], vertices[0], vertices[4]],
                                [vertices[0], vertices[1], vertices[2], vertices[3]],
                                ]

                            poly3d = Poly3DCollection(faces, facecolors=color, linewidths=1, edgecolors='black', alpha=alpha)
                            ax.add_collection3d(poly3d)
                        
                        
                        


                         #Buildings

                        ax.bar3d(0,-5,0.1,2.9,2.9,1.7, color = 'grey', alpha =0.9) #Workshop
                        ax.bar3d(10,-5,0.1,2.9,2.9,1.7, color = 'grey', alpha =0.9) #Garage
                        ax.bar3d(25,-5,0.1,3.3,3.9,4.7, color = 'grey', alpha =0.9) #Warehouse
                        ax.bar3d(-10,-5,0.1,2.9,2.9,1.7, color = 'yellow', alpha =0.9) #Transformer

                        # Conveyor Platform
                        ax.plot([0, 40], [0, 0], [0, 0], color='black', linewidth=5, label='Conveyor Belt')
                        ax.bar3d(0, -1, 0, 40, 2, 0.1, color='grey', alpha=0.25)

                         # Processing Units
                        draw_trapezoid_upside_down(ax, 5, 0, 0.1, 1.5, 1.5, 2.1, color='violet')       # Shredder
                        ax.bar3d(5, 0, 0.1, 1.5, 1.5, 1.45, color='violet', alpha=0.9)                 #Shredder
                        draw_trapezoid_upside_down(ax, 9.5, 0, 0.1, 1.5, 1.5, 2.1, color='steelblue')  # Crusher
                        draw_trapezoid_upside_down(ax, 19, 0, 0.1, 1.5, 1.5, 2.1, color='purple')      # Grinder
                        draw_trapezoid_upside_down(ax, 18, 6, 0, 2, 2, 4, color='gold')                # Electrostatic Precipitator
                        draw_trapezoid_upside_down(ax, 30, 6, 0, 2, 2, 4, color='gold')                # Electrostatic Precipitator
                        draw_triangular_prism(ax, base_center=(19, 7, 4), width=2, depth=2, height=4, color='gold', alpha=0.9) # Electrostatic Precipitator
                        draw_triangular_prism(ax, base_center=(31, 7, 4), width=2, depth=2, height=4, color='gold', alpha=0.9) #Electrostatic Precipitator
    
                        #Air-flow separator
                        ax.bar3d(15, 0, 0.1, 1.4, 1.6, 2.2, color='silver', alpha=0.9) 
                        #Compressor
                        create_cylinder(6,6+1,0,4,1,'green',ax)# Compressor

                        # Pipes
                        ax.plot([6, 15], [6, 1], [4, 2.2], color='blue', linewidth=3)
                        ax.plot([15, 18], [0, 6], [2.2, 4], color='blue', linewidth=3)
                        ax.plot([18, 30], [6, 6], [4, 4], color='blue', linewidth=3)
    
                        #Towers
                        draw_trapezoid(ax, -10, -20, 0.1, 2.5, 1.05, 4.5, color='steelblue')
                        draw_trapezoid(ax, -10, -10, 0.1, 2.5, 1.05, 4.5, color='steelblue')
                        draw_trapezoid(ax, -10, 0, 0.1, 2.5, 1.05, 4.5, color='steelblue')
                        draw_trapezoid(ax, -10, 10, 0.1, 2.5, 1.05, 4.5, color='steelblue')

                         # Wires
                        ax.plot([-10, -10], [-20, -10], [4.5, 4.5], color='brown', linewidth=3)
                        ax.plot([-10, -10], [-10, 0], [4.5, 4.5], color='brown', linewidth=3)
                        ax.plot([-10, -10], [-10, 10], [4.5, 4.5], color='brown', linewidth=3)

                        # Plot the rail-line
                        for i in range(0, 50, 2):
                            ax.plot([i, i], [-14, -12], [0, 0], color='grey')
                            ax.plot([-4, 50], [-13.75, -13.75], [0, 0], color='black', linewidth=2)
                            ax.plot([-4, 50], [-12.75, -12.75], [0, 0], color='black', linewidth=2)

                        # Plot the road
                        for i in range(0, 50, 2):
                            ax.plot([i, i],[-9.5, -9.5], [0,0], color = 'white')
                            ax.plot([-4, 50], [-9.8, -9.8], [0, 0], color = 'black', linewidth =4)
                            ax.plot([-4, 50], [-9.6, -9.6], [0, 0], color = 'black', linewidth =4)
                            ax.plot([-4, 50], [-9.4, -9.4], [0, 0], color = 'black', linewidth =4)
                            ax.plot([-4, 50], [-9.2, -9.2], [0, 0], color = 'black', linewidth =4)
                            ax.plot([-4, 50], [-9, -9], [0, 0], color = 'black', linewidth =4)
                            ax.plot([-4, 50], [-8.8, -8.8], [0, 0], color = 'black', linewidth =4)
                            ax.plot([-4, 50], [-8.6, -8.6], [0, 0], color = 'black', linewidth =4)
                        
                        # Air particles
                        for T in Air_particles:
                            Tx = 6 + (T / 9.5) * (15 - 6)
                            Ty = 6 - (T / 9.5) * (6 - 1)
                            Tz = 4 - (T / 9.5) * (4 - 2.5)
                            ax.scatter(Tx, Ty, Tz, color='cyan', s=30)

                        # Organic particles
                        for P in Organic_particles:
                            Px = 15 + (P / 10) * (18 - 15)
                            Py = 0 + (P / 10) * (6 - 0)
                            Pz = 2.2 + (P / 10) * (4 - 2.2)
                            ax.scatter(Px, Py, Pz, color='magenta', s=30)

                         # Electron flow
                        for E in Electron:
                            Ex = -10
                            Ey = 10 + (E / 8) * (-20 + 10)
                            Ez = 4.5
                            ax.scatter(Ex, Ey, Ez, color='silver', s=3)
        
                        # Flowing Organic particles from Precipitator 1 → Precipitator 2
                        for Q in Organic_particles:
                            Qx = 18 + (Q / 10) * (30 - 18)
                            Qy = 6
                            Qz = 4
                            ax.scatter(Qx, Qy, Qz, color='magenta', s=30)
                        # Crystals on Conveyor
                        for pos in crystal_positions:
                            draw_trapezoid_upside_down(ax, pos, 0, 0.1, 1, 1, 0.8, color='orange')

                        # Move Air particles
                        for T in range(len(Air_particles)):
                            Air_particles[T] += 0.2
                            if Air_particles[T] > 10:
                                Air_particles[T] = 0

                        # Move Organic particles
                        for P in range(len(Organic_particles)):
                            Organic_particles[P] += 0.4
                            if Organic_particles[P] > 10:
                                Organic_particles[P] = 0


                        # Move Electrons
                        for E in range(len(Electron)):
                            Electron[E] += 0.5
                            if Electron[E] > 24:
                                Electron[E] = 0

                        handles, labels = ax.get_legend_handles_labels()
                        by_label = dict(zip(labels, handles))
                        ax.legend(by_label.values(), by_label.keys(), loc='upper left')

                        canvas.draw() 

                    def update():
                        for i in range(len(crystal_positions)):
                            crystal_positions[i] += 0.3
                            if crystal_positions[i] > 40:
                                crystal_positions[i] = 0
                        draw_plant(ax)
                        root.after(100, update)   
                    # Tkinter Setup
                    root = tk.Tk()
                    root.title(" Plant Simulation")

                    fig = Figure(figsize=(10, 7))
                    ax = fig.add_subplot(111, projection='3d')
                    canvas = FigureCanvasTkAgg(fig, master=root)
                    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

                    draw_plant(ax)
                    update()

                    root.mainloop()            
                except ValueError:
                    label_action1.config(root,text ='Error')    



                        
        
                except ValueError:
                    label_action1.config(text = 'Error')                         
            except ValueError:
                label_action1.config(text = 'Error')
    

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


# Initialize prompt
update_prompt(
    'What do you want to do? (explore narrow tunnel/enter mining equipment room/enter substation room/leave):',
    ('explore narrow tunnel', 'enter mining equipment room', 'enter substation room', 'leave')
)

root.mainloop()
