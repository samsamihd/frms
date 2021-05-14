import React, { useEffect, useState } from "react";
import axios, { AxiosRequestConfig } from "axios";
import { LatLngExpression } from "leaflet";
import { GeoJSON, MapContainer, TileLayer } from "react-leaflet";
import SideBar from "./SideBar";

const Home = () => {
  const defaultPosition: LatLngExpression = [35.641638, 47.817199];
  const token: string = JSON.parse(localStorage.getItem("token") || "{}");
  const [features, setFeatures] = useState<any>();
  const [floodPlain, setFloodplain] = useState<any>();
  const [events, setEvents] = useState<Array<string>>([]);
  const [event, setEvent] = useState<string>("");

  const getEvents = async () => {
    let config: AxiosRequestConfig = {
      method: "get",
      url: `${process.env.REACT_APP_BACKEND_URL}/api/floodplains/events`,
      headers: {
        Authorization: `Token ${token}`,
        "Content-Type": "application/x-www-form-urlencoded",
      },
    };
    await axios(config)
      .then(async function (response) {
        setEvents(response.data.data.events);
        setEvent(response.data.data.events[0]);
      })
      .catch(function (error) {
        console.log(error);
      });
  };

  const getFeatures = async (dateItem: any) => {
    if (dateItem !== "") {
      let config: AxiosRequestConfig = {
        method: "get",
        url: `${process.env.REACT_APP_BACKEND_URL}/api/features/${dateItem}/`,
        headers: {
          Authorization: `Token ${token}`,
          "Content-Type": "application/x-www-form-urlencoded",
        },
      };
      await axios(config)
        .then(async function (response) {
          setFeatures(JSON.parse(response.data.data));
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  };

  const getFloodplain = async (dateItem: any) => {
    if (dateItem !== "") {
      let config: AxiosRequestConfig = {
        method: "get",
        url: `${process.env.REACT_APP_BACKEND_URL}/api/floodplains/detail/${dateItem}/`,
        headers: {
          Authorization: `Token ${token}`,
          "Content-Type": "application/x-www-form-urlencoded",
        },
      };
      await axios(config)
        .then(async function (response) {
          setFloodplain(JSON.parse(response.data.data));
        })
        .catch(function (error) {
          console.log(error);
        });
    }
  };

  useEffect(() => {
    getEvents();
  }, []);

  useEffect(() => {
    getFloodplain(event);
    getFeatures(event);
  }, [event]);

  const abc = () => {
    return Math.random().toString(36).substring(7);
  };

  return (
    <React.Fragment>
      <header className="navbar navbar-light sticky-top bg-white flex-md-nowrap p-0 shadow">
        <a className="navbar-brand col-md-3 col-lg-2 me-0 px-3" href="#">
          FRMS
        </a>
        <div className="d-flex justify-content-between w-100">
          <button
            className="navbar-toggler position-absolute d-md-none collapsed"
            type="button"
            data-bs-toggle="collapse"
            data-bs-target="#sidebarMenu"
            aria-controls="sidebarMenu"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <input
            className="form-control form-control-dark w-25"
            type="text"
            placeholder="Search"
            aria-label="Search"
          />
          <ul className="navbar-nav px-3">
            <li className="nav-item text-nowrap">
              <a className="nav-link" href="#">
                Sign out
              </a>
            </li>
          </ul>
        </div>
      </header>
      <div className="container-fluid">
        <div className="row">
          <SideBar features={features} />
          <main className="position-relative col-md-9 ms-sm-auto col-lg-10 m-0 p-0">
            <MapContainer center={defaultPosition} zoom={13}>
              <TileLayer
                attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
              />
              <GeoJSON
                key={abc()}
                data={features}
                pathOptions={{
                  color: "red",
                  weight: 1,
                  opacity: 0.5,
                  fillOpacity: 0.5,
                }}
              />
              <GeoJSON
                key={abc()}
                data={floodPlain}
                pathOptions={{ color: "blue", stroke: false }}
              />
            </MapContainer>
            <div
              className="position-absolute d-flex justify-content-center w-100"
              style={{ bottom: 20, left: 0, zIndex: 1000 }}
            >
              {events.length > 0 ? (
                events.map((eventItem: any, index: number) => {
                  return (
                    <div
                      key={index}
                      className={
                        eventItem === event
                          ? "mx-2 p-2 rounded-circle bg-primary border border-secondary border-2 shadow-sm"
                          : "mx-2 p-2 rounded-circle bg-light border border-secondary border-2 shadow-sm"
                      }
                      onClick={() => setEvent(eventItem)}
                      title={eventItem}
                      data-bs-toggle="tooltip"
                      data-bs-placement="top"
                    />
                  );
                })
              ) : (
                <React.Fragment />
              )}
            </div>
          </main>
        </div>
      </div>
    </React.Fragment>
  );
};

export default Home;
