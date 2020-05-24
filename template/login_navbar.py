import dash_bootstrap_components as dbc

def Navbar():
      navbar = dbc.NavbarSimple(
        [
              dbc.NavItem(dbc.NavLink("Company Signup", href="/company-signup")),
              dbc.NavItem(dbc.NavLink("Candidate Signup", href="/candidate-signup"))
       ],
          brand="Home",
          brand_href="/login-to-home",
          sticky="top",
        )
      return navbar