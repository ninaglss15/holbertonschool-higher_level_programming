document.addEventListener("DOMContentLoaded", async () => {
    const element = document.getElementById("hello");

    async function getData() {
        const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";
        try {
            const response = await fetch(url);
            if (!response.ok) {
                throw new Error(`Response status: ${response.status}`);
            }
      
            const json = await response.json();
            element.textContent = json.hello;
        } catch (error) {
            console.error(error.message);
        }
    }

    getData();
});