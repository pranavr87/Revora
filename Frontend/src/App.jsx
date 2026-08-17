import { BrowserRouter, Routes, Route } from "react-router-dom";

import Landing from "./pages/Landing";
import Diagnosis from "./pages/Diagnosis";

function App() {
    return (
        <BrowserRouter>

            <Routes>

                <Route
                    path="/"
                    element={<Landing />}
                />

                <Route
                    path="/diagnosis"
                    element={<Diagnosis />}
                />

            </Routes>

        </BrowserRouter>
    );
}

export default App;