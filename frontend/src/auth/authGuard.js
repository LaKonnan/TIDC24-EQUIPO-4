import { getInstance } from "./index";
//import { getAPI } from '../components/axios-api';

export const authGuard = (to, from, next) => {
  const authService = getInstance();

  const fn = async () => {
    // If the user is authenticated, continue with the route
    if (authService.isAuthenticated) {

      /*const rol = await getAPI.get('/rol/'+ authService.user.sub)
      .then(response => {
          return response.data.roles[0].name
      })
      .catch(err => {
          console.log(err)
      })
      
      if(
        to.path == '/' ||
        to.path == '/no-access' ||
        to.path == '/login' ||
        to.path == '/cajas-chicas' ||
        to.path == '/maquinas' ||
        to.path == '/reglamento' ||
        (rol == 'admin' && to.path=='/usuarios') ||
        ((rol == 'admin' || (rol == 'gerente') || (rol == 'encargado')) && to.path=='/obras')
      ){*/
        return next()
      /*} else {
        return next('/no-access')
      }*/
    }

    // Otherwise, log in
    authService.loginWithRedirect({ appState: { targetUrl: to.fullPath } });
  };

  // If loading has already finished, check our auth state using `fn()`
  if (!authService.loading) {
    return fn();
  }

  // Watch for the loading property to change before we check isAuthenticated
  authService.$watch("loading", loading => {
    if (loading === false) {
      return fn();
    }
  });
};