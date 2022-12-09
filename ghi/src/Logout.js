import { useToken } from "./GetToken";
import { useNavigate } from "react-router-dom";

function Logout() {
    const [, , logout] = useToken();
    console.log("logout::", logout)
    // console.log("login::", login)

    const navigate = useNavigate();
    // const { token } = useAuthContext();


    const handleSubmit = async (e) => {
        e.preventDefault();
        logout();
        navigate("/");
    }

}

export default Logout;
