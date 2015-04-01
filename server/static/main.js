$(document).ready()
{
	var adresse = $("#optionsCheckbox1")
	var coordonnees = $("#optionsCheckbox2")
	var adresseCol = $("#adresseCol")
	var coordonneesCol = $("#coordCol")

	if(document.getElementsByName('optionsCheckbox')[0].checked & !(document.getElementsByName('optionsCheckbox')[1].checked))
	{
		adresseCol.show()
		coordonneesCol.hide()
	}
	else if (!(document.getElementsByName('optionsCheckbox')[0].checked) & document.getElementsByName('optionsCheckbox')[1].checked) 
	{
		adresseCol.hide()
		coordonneesCol.show()
	}
	else if (document.getElementsByName('optionsCheckbox')[0].checked & document.getElementsByName('optionsCheckbox')[1].checked) 
	{
		adresseCol.show()
		coordonneesCol.show()
	}
	else if (!(document.getElementsByName('optionsCheckbox')[0].checked) & !(document.getElementsByName('optionsCheckbox')[1].checked)) 
	{	
		adresseCol.hide()
		coordonneesCol.hide()
	}
}