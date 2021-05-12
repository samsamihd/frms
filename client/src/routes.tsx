import { Route, Switch } from "react-router-dom";
import Home from "./components/Home";

const AppRouter = () => (
  <Switch>
    <Route path="/">
      <Home />
    </Route>
  </Switch>
);

export default AppRouter;
