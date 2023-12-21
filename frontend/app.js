const insertOsobaUrl = 'http://127.0.0.1:5000/insert_osoba';
const insertBrakUrl = 'http://127.0.0.1:5000/insert_brak';

async function predaj(){
    var form = document.getElementsByTagName('form')[0];
    
    const muzData = {
        ime: form[0].value,
        prezime: form[1].value,
        zanimanje: form[2].value,
        mestoRodjenja: form[3].value,
        godinaRodjenja: form[4].value,
        drzavljanstvo: form[5].value,
        imePrezimeRoditelji: form[12].value
    };

    const zenaData = {
        ime: form[6].value,
        prezime: form[7].value,
        zanimanje: form[8].value,
        mestoRodjenja: form[9].value,
        godinaRodjenja: form[10].value,
        drzavljanstvo: form[11].value,
        imePrezimeRoditelji: form[13].value
    };

    try {
        const idMuza = await postOsoba(insertOsobaUrl, muzData);
        const idZene = await postOsoba(insertOsobaUrl, zenaData);

        const brakData = {
            idOsobe1: idMuza['id'],
            idOsobe2: idZene['id'],
            brakSklopljen: form[14].value,
            brakPoRedu: form[15].value,
            mestoVencanja: form[16].value,
            koJeVencao: form[17].value,
            svedoci: form[18].value
        };
        
        ans = await postBrak(insertBrakUrl, brakData);
        console.log(ans);

    } catch (error) {
        console.error('Error:', error);
        return
    }
}


async function postOsoba(url, data) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        return result['id'];
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
};

async function postBrak(url, data) {
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();
        return (result);
    } catch (error) {
        console.error('Error:', error);
    }
};
