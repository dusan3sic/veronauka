const insertOsobaUrl = 'http://127.0.0.1:5000/insert_osoba';
const insertBrakUrl = 'http://127.0.0.1:5000/insert_brak';

class Er extends Error {
    constructor(message, statusCode) {
        super(message);
        this.name = "moj error";
        this.code = statusCode;
    }
}

async function predaj(){
    var form = document.getElementsByTagName('form')[0];

    let puna = highlightEmptyFields(form);
    if(!puna) return;
    
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

        if(idMuza == null || idZene == null) throw new Er("idMuza ili idZene ne postoji", 503);

        const brakData = {
            idOsobe1: idMuza,
            idOsobe2: idZene,
            brakSklopljen: form[14].value,
            brakPoRedu: form[15].value,
            mestoVencanja: form[16].value,
            koJeVencao: form[17].value,
            svedoci: form[18].value
        };
        
        let ans = await postBrak(insertBrakUrl, brakData);
        if(ans == null) throw new Er("Brak nije uspostavljen", 503);

        if(ans['code'] == 200) uspesnaForma(form);
        else throw new Er(ans["error"], ans['code']);

    } catch (error) {
        if(error.code == 503) alert("Veza sa serverom nije uspostavljena!");
        else if(error.code == 409) alert("Pokusavata da unesete brak koji vec postoji!");
        
        console.log(error.message);
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


function uspesnaForma(form){
    console.log("uspesna forma");

    form.reset();
}

function highlightEmptyFields(form) {
    let firstEmptyField = null;


    let emptyCnt = 0;
    for (let i = 0; i < form.length; i++) {
        const field = form[i];

        if (field.tagName !== 'INPUT')  continue;

        if (!field.value.trim()) {
            field.style.border = '2px solid red';
            emptyCnt += 1

            if (!firstEmptyField) firstEmptyField = field;
        } else field.style.border = '';
    }

    if (firstEmptyField)  firstEmptyField.focus();

    return (emptyCnt == 0);
}