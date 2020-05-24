import dash_bootstrap_components as dbc

def Navbar():
      navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dbc.NavLink("Candidate Info", href="/analytics-candidate-info")),
              dbc.NavItem(dbc.NavLink("Company Info", href="/analytics-company-info")),
              dbc.NavItem(dbc.NavLink("Logout", href="/logout"))
            ],
          brand="Home",
          brand_href="/home",
          sticky="top",
        )
      return navbar
