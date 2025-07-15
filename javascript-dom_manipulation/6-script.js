const element = document.getElementById("character");


  async function getData() {
    const url = "https://swapi-api.hbtn.io/api/people/5/?format=json";
    try {
      const response = await fetch(url);
      if (!response.ok) {
        throw new Error(`Response status: ${response.status}`);
      }
  
      const json = await response.json();
      element.textContent = json.name
    } catch (error) {
      console.error(error.message);
    }
  }

  getData();