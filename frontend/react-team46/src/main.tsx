import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { Auth0Provider } from "@auth0/auth0-react"; // Import Auth0Provider
import "./index.css";
import App from "./App.tsx";
import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";

// Get the values from environment variables (make sure they're in the .env file)
const authDomain = import.meta.env.VITE_AUTH0_DOMAIN;
const clientId = import.meta.env.VITE_AUTH0_CLIENT_ID;
const callbackUrl = import.meta.env.VITE_AUTH0_CALLBACK_URL; // Optional, only if you need to customize
const audience = import.meta.env.VITE_AUTH0_AUDIENCE; // Optional, only if you need to set an audience

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <Auth0Provider
      domain={authDomain}
      clientId={clientId}
      authorizationParams={{
        redirect_uri: window.location.origin + callbackUrl, // Handle redirect URL
      }}
    >
      <App />
    </Auth0Provider>
  </StrictMode>
);
