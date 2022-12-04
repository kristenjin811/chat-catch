import { useState } from "react";

const MessageForm = () => {
  const [message, setMessage] = useState("");
  const [submitted, setSubmittedMessage] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();
    const data = { message };

    const url = "http://localhost:8000/api/chatrooms/";
    const fetchConfig = {
      method: "POST",
      body: JSON.stringify(data),
      headers: {
        "Content-Type": "application/json",
      },
    };

    const response = await fetch(url, fetchConfig);
    if (response.ok) {
      event.target.reset();
      setMessage("");
      setSubmittedMessage(true);
    }
  };

  return (
    <div className="row">
      <div className="offset-3 col-6">
        <div className="shadow p-4 mt-4">
          <h1 className="text-center">Create a Message</h1>
          <form id="create-message-form" onSubmit={handleSubmit}>
            <div className="form-floating mb-3">
              <input
                onChange={(e) => setMessage(e.target.value)}
                placeholder="Message"
                required
                type="text"
                name="message"
                id="message"
                className="form-control"
              />
              <label htmlFor="message">Message</label>
            </div>
            <div className="col text-center">
              <button className="btn btn-primary">Create Message</button>
            </div>
          </form>
          {submitted && (
            <div
              className="alert alert-success mb-0 p-4 mt-4"
              id="success-message"
            >
              Your message has been created!
            </div>
          )}
        </div>
      </div>
    </div>
  );
};
export default MessageForm;
