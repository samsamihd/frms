import { Navigate, Route, Outlet, Routes } from "react-router-dom";
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
  const PrivateRoute = () => {
    const auth = isLoggedIn();
    return auth ? <Outlet /> : <Navigate to="/login" replace />;
  };
  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route path="/" element={<PrivateRoute />}>
        <Route path="/" element={<Home />} />
      </Route>
    </Routes>
  );
};

export default AppRouter;
