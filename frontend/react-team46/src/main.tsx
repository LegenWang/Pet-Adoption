import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { Auth0Provider } from "@auth0/auth0-react";
import "./index.css";
import App from "./App.tsx";
import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const authDomain = import.meta.env.VITE_AUTH0_DOMAIN;
const clientId = import.meta.env.VITE_AUTH0_CLIENT_ID;
const callbackUrl = import.meta.env.VITE_AUTH0_CALLBACK_URL;
const audience = import.meta.env.VITE_AUTH0_AUDIENCE;

if (!authDomain || !clientId || !callbackUrl) {
  console.error('Missing Auth0 configuration');
}

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Auth0Provider
      domain={authDomain}
      clientId={clientId}
      authorizationParams={{
        redirect_uri: callbackUrl,
        audience: audience,
        scope: "openid profile email"
      }}
    >
      <App />
    </Auth0Provider>
  </StrictMode>
);