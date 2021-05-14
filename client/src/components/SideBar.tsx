import React from "react";
import FeatureCard from "./FeatureCard";

const SideBar = (props: any) => {
  console.log(props.features);
  return (
    <nav
      id="sidebarMenu"
      className="col-md-3 col-lg-2 d-md-block bg-white sidebar collapse"
    >
      {props.features ? (
        <div className="mt-4">
          {props.features.features.map((feature: any) => {
            return <FeatureCard feature={feature.properties} />;
          })}
        </div>
      ) : (
        <React.Fragment />
      )}
    </nav>
  );
};

export default SideBar;
