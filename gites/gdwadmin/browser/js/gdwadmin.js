
function passage(lieu){
 document.info.nom_objet.value=lieu;
}


function ouvrir_fenetre(site){
	nav=window.open(site,'fenetre', 'height=250, width=400, left=700, top=30, status=no, menubar=no, scrollbars=no, resizable=no');
	nav.setTimeout("window.close()",10000);
}

function ouvrir_gallerie(site){
	nav=window.open(site,'fenetre', 'height=550, width=350, left=670, top=30, status=no, menubar=no, scrollbars=yes, resizable=yes');
}

function test(){
	alert('ici');
}

function fermer_fenetre(){
	self.close();
}


function Envoyer(op){
   if (op=='modifier'){
      document.formulaire.operation.value="modifier";
      document.formulaire.submit();
   }
   if (op=='supprimer'){
      document.formulaire.operation.value="supprimer";
      document.formulaire.submit();
   }
   if (op=='creer'){
      document.formulaire_creation.submit();
   }

}

$(document).ready(function()
    {
        $("#table-listing-localites").tablesorter();
        $("#table-listing-communes-francophones").tablesorter();
        $("#table-listing-communes-neerlandophones").tablesorter();
        $("#table-listing-communes-etrangeres").tablesorter();
    }
);
