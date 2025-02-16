import tableauserverclient as TSC

def refresh_tableau_datasource():
    # Tableau Server authentication
    tableau_auth = TSC.TableauAuth('username', 'password')
    server = TSC.Server('https://tableau.company.com')
    
    with server.auth.sign_in(tableau_auth):
        # Find and refresh specific datasource
        all_datasources = list(TSC.Datasources(server))
        for datasource in all_datasources:
            if datasource.name == 'Sales_Dashboard_DS':
                server.datasources.refresh(datasource)
