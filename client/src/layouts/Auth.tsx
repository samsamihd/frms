const Auth = (props: any) => {
  return (
    <div className="container">
      <div className="row" style={{ marginTop: "20%" }}>
        <div className="col-md-6 mx-auto bg-white p-3 rounded">
          <h1 className="logo text-center" style={{ fontSize: "2.5em" }}>
            FRMS
          </h1>
          {props.content}
        </div>
      </div>
    </div>
  );
};

export default Auth;
