import {
  Redirect,
  Route,
  RouteChildrenProps,
  RouteComponentProps,
  Switch,
} from "react-router-dom";
import Auth from "./layouts/Auth";
import Login from "./components/User/Login";
import Home from "./components/Home";

const AppRouter = () => {
  const isLoggedIn = () => {
    const token: string = JSON.parse(localStorage.getItem("token") || "{}");
    if (token) {
      return true;
    } else {
      return false;
    }
  };
  interface RouteProps {
    component?:
      | React.ComponentType<RouteComponentProps<any>>
      | React.ComponentType<any>;
    render?: (props: RouteComponentProps<any>) => React.ReactNode;
    children?:
      | ((props: RouteChildrenProps<any>) => React.ReactNode)
      | React.ReactNode;
    path?: string | string[];
    exact?: boolean;
    sensitive?: boolean;
    strict?: boolean;
  }
  const PrivateRoute = ({ component: Component, ...rest }: RouteProps) => {
    if (!Component) return null;
    return (
      <Route
        {...rest}
        render={(props) =>
          isLoggedIn() === true ? (
            <Component {...props} />
          ) : (
            <Redirect to="/login" />
          )
        }
      />
    );
  };
  return (
    <Switch>
      <Route exact path="/login" render={() => <Auth content={<Login />} />} />
      <PrivateRoute exact path="/" component={Home} />
    </Switch>
  );
};

export default AppRouter;
