import parser from "@babel/eslint-parser";  // Correct parser import
import reactHooks from "eslint-plugin-react-hooks";
import reactRefresh from "eslint-plugin-react-refresh";
import tseslint from "@typescript-eslint/eslint-plugin";

export default [
  {
    files: ["**/*.{ts,tsx}"],
    languageOptions: {
      parser,  // Use @babel/eslint-parser for JSX and TSX support
      ecmaVersion: 2020,
      globals: {
        browser: true,  // Define the browser global directly here
      },
      parserOptions: {
        ecmaFeatures: {
          jsx: true,  // Enable JSX parsing
        },
        project: './tsconfig.json',  // If you're using TypeScript, add this line
      },
    },
    plugins: {
      "react-hooks": reactHooks,
      "react-refresh": reactRefresh,
      "@typescript-eslint": tseslint,
    },
    rules: {
      ...reactHooks.configs.recommended.rules,
      "react-refresh/only-export-components": [
        "warn",
        { allowConstantExport: true },
      ],
    },
  },
];
