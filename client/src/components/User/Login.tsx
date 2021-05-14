import React, { useState } from "react";
import axios from "axios";
import Qs from "qs";
import { useHistory } from "react-router-dom";
import { useForm } from "react-hook-form";

function Login() {
  const history = useHistory();
  const { register, handleSubmit } = useForm();
  const [message, setMessage] = useState("");

  const handleLogin = async (loginData: {
    username: string;
    password: string;
  }) => {
    let config: any = {
      method: "post",
      url: `${process.env.REACT_APP_BACKEND_URL}/auth-token/`,
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
      data: Qs.stringify(loginData),
    };
    await axios(config)
      .then(function (response) {
        localStorage.setItem("token", JSON.stringify(response.data.token));
        history.push("/");
        window.location.reload();
      })
      .catch(function (error) {
        console.log(error);
        setMessage(
          `Error ${error.response.status}: ${error.response.statusText}`
        );
      });
  };

  return (
    <main>
      <h5 className="text-center text-secondary">Login</h5>
      {message ? (
        <div className="alert alert-danger" role="alert">
          {message}
        </div>
      ) : (
        <React.Fragment />
      )}
      <form onSubmit={handleSubmit(handleLogin)}>
        <div className="mb-3">
          <label htmlFor="exampleInputEmail1" className="form-label">
            Email address
          </label>
          <input
            type="email"
            className="form-control"
            id="exampleInputEmail1"
            aria-describedby="emailHelp"
            required
            {...register("username")}
          />
          <div id="emailHelp" className="form-text">
            We'll never share your email with anyone else.
          </div>
        </div>
        <div className="mb-3">
          <label htmlFor="exampleInputPassword1" className="form-label">
            Password
          </label>
          <input
            type="password"
            className="form-control"
            id="exampleInputPassword1"
            {...register("password")}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">
          Submit
        </button>
      </form>
    </main>
  );
}

export default Login;
