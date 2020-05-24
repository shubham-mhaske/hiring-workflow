import dash_bootstrap_components as dbc

def Navbar():
      navbar = dbc.NavbarSimple(
           children=[
              
              dbc.NavItem(dbc.NavLink("Jobs", href="/jobs")),
              dbc.NavItem(dbc.NavLink("My Applications", href="/candidate-my-profile")),
              dbc.NavItem(dbc.NavLink("Logout", href="/logout"))
   
                    ],
          brand="Home",
          brand_href="/home",
          sticky="top",
        )
      return navbar