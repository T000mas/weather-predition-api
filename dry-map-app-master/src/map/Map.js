import React from "react";
import { useEffect, useState } from "react";
import MapGL, { Source, Layer } from "react-map-gl";
import mapGrid from "./consts/map-grid.json";
import { dataLayer } from "./utils/data-layer";

function Map() {
  const [viewport, setViewport] = useState({
    longitude: 14.1488,
    latitude: 48.73,
    zoom: 5,
    width: window.innerWidth,
    height: window.innerHeight,
  });
  const [data, setData] = useState([]);
  const [info, setInfo] = useState(null);

  const layerStyle = {
    id: "data",
    type: "fill",
    paint: {
      "fill-color": {
        property: "temperature",
        stops: [
          [0, "#091be3"],
          [4, "#0aa1ff"],
          [8, "#0afff7"],
          [14, "#09ed2f"],
          [20, "#ffe70a"],
          [30, "#ff0a0a"],
        ],
      },
      "fill-opacity": 0.8,
    },
  };

  useEffect(() => {
    const lengthConst = 0.4;
    const latitConst = 0.24;
    const cities = [
      "Warsaw",
      "Berlin",
      "Prague",
      "Paris",
      "Budapest",
      "Brussels",
      "Vienna",
      "Cluj-Napoca",
      "Zürich",
      "Frankfurt",
      "San Marino",
      "Hamburg",
      "Ahmadabad",
      "Bangkok",
    ];
    cities.forEach((city) => {
      fetch(`http://localhost:7001/weatherByCity/?city=${city}`)
        .then((res) =>
          res.json().then((resData) => {
            // http://127.0.0.1:7002/simplePrediction/getPredictionByCity/?city=Ahmadabad
            fetch(
              `http://127.0.0.1:7002/simplePrediction/getPredictionByCity/?city=${city}`
            )
              .then((res2) =>
                res2.json().then((resData2) => {
                  // http://127.0.0.1:7002/simplePrediction/getPredictionByCity/?city=Ahmadabad

                  const feature = {
                    type: "Feature",
                    geometry: {
                      type: "Polygon",
                      coordinates: [
                        [
                          [
                            resData["longitude"] - lengthConst,
                            resData["latitude"] - latitConst,
                          ],
                          [
                            resData["longitude"] + lengthConst,
                            resData["latitude"] - latitConst,
                          ],
                          [
                            resData["longitude"] + lengthConst,
                            resData["latitude"] + latitConst,
                          ],
                          [
                            resData["longitude"] - lengthConst,
                            resData["latitude"] + latitConst,
                          ],
                        ],
                      ],
                    },
                    properties: {
                      temperature: resData["temp"],
                      name: city,
                      probability: resData2["probability"],
                    },
                  };
                  // console.log(resData2["probability"]);
                  setData((oldData) => [...oldData, feature]);
                })
              )
              .catch((error) => {
                console.error(error);
              });
            // const feature = {
            //   type: "Feature",
            //   geometry: {
            //     type: "Polygon",
            //     coordinates: [
            //       [
            //         [
            //           resData["longitude"] - lengthConst,
            //           resData["latitude"] - latitConst,
            //         ],
            //         [
            //           resData["longitude"] + lengthConst,
            //           resData["latitude"] - latitConst,
            //         ],
            //         [
            //           resData["longitude"] + lengthConst,
            //           resData["latitude"] + latitConst,
            //         ],
            //         [
            //           resData["longitude"] - lengthConst,
            //           resData["latitude"] + latitConst,
            //         ],
            //       ],
            //     ],
            //   },
            //   properties: { temperature: resData["temp"], name: city },
            // };
            // setData((oldData) => [...oldData, feature]);
          })
        )
        .catch((error) => {
          console.error(error);
        });
    });
  }, []);

  useEffect(() => {
    console.log(data);
  }, [data]);

  const onClick = (event) => {
    // useCallback(event => {
    const {
      features,
      srcEvent: { offsetX, offsetY },
    } = event;
    const hoveredFeature = features && features[0];
    console.log(hoveredFeature);
    setInfo(hoveredFeature);
    // console.log(offsetX);
    // console.log(offsetY);
  };

  function getCursor({ isHovering, isDragging }) {
    return isDragging ? "grabbing" : isHovering ? "pointer" : "default";
  }

  return (
    <div>
      <MapGL
        {...viewport}
        mapboxApiAccessToken="pk.eyJ1IjoiYXZlbHVkb3dpayIsImEiOiJja3ZvODAxdXYwcnZsMnBqcGFsdGFvYnpsIn0.GXnlJJJPUArw7jszNQJ0eQ"
        onViewportChange={(viewport) => setViewport(viewport)}
        mapStyle="mapbox://styles/mapbox/light-v9"
        onClick={onClick}
        getCursor={getCursor}
        interactiveLayerIds={["data"]}
      >
        <Source
          id="test"
          type="geojson"
          data={{ type: "FeatureCollection", features: data }}
        >
          <Layer {...layerStyle} />
        </Source>
      </MapGL>
      <div
        style={{
          background: "gray",
          color: "white",
          position: "fixed",
          bottom: 0,
          right: 0,
          height: "10%",
          width: "15%",
          padding: 10,
        }}
      >
        {info && (
          <div>
            <div>City: {info.properties["name"]}</div>
            <div>Temperature: {info.properties["temperature"]}°C</div>
            <div>Drought probability: {info.properties["probability"]}</div>
          </div>
        )}
      </div>
    </div>
  );
}
export default Map;
