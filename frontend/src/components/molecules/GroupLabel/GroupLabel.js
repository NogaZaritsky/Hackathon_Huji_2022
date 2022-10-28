import React from "react";
import { useState } from "react";
import "./GroupLabel.css";
import { Avatar } from "@mui/material";

function GroupLabel() {
  const [data, setData] = useState([
    {
      subject: "Infi 2",
      datetime: "04/04/22 16:00",
    },
  ]);

  const pic = "";
  return (
    <div className="groupLabel" key={data.subject}>
      {data.map((lbl) => (
        <div>
          <Avatar alt={lbl.subject} src={pic} sx={{ width: 50, height: 50 }} />
          <p style={{ padding: "10px" }}>{lbl.subject}</p>
          <p>{lbl.datetime}</p>
        </div>
      ))}
    </div>
  );
}

export default GroupLabel;
