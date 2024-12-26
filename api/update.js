let message = "";

export default function handler(req, res) {
    if (req.method === 'POST') {
        const { command } = req.body;
        if (command === "/ping") {
            message = "!pong";
        }
        return res.status(200).json({ success: true });
    } else if (req.method === 'GET') {
        return res.status(200).json({ message });
    } else {
        return res.status(405).json({ error: "Method Not Allowed" });
    }
}
