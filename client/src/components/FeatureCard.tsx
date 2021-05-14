import React from "react";

const SideBar = (props: any) => {
  return (
    <div className="card mb-2">
      <div className="card-body">
        <h4 className="card-title">{props.feature.title}</h4>
        <p className="card-text">
          <b>Attendant: </b>
          {props.feature.attendant}
        </p>
        <p className="card-text">
          <b>Phone: </b>
          {props.feature.phone}
        </p>
        <a href="#" className="btn btn-primary">
          Send Message
        </a>
      </div>
    </div>
  );
};

export default SideBar;
