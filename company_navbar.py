import dash_bootstrap_components as dbc

def Navbar():
      navbar = dbc.NavbarSimple(
           children=[
              dbc.NavItem(dbc.NavLink("Applications", href="/applications")),
              dbc.NavItem(dbc.NavLink("Post Job", href="/add-new-job")),
              dbc.NavItem(dbc.NavLink("Logout", href="/logout"))
              

                    ],
          brand="Home",
          brand_href="/home",
          sticky="top",
        )
      return navbar