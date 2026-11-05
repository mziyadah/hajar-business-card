from pathlib import Path
from PIL import Image, ImageOps
from io import BytesIO
import base64
im=Image.open("Image.jpg").convert("RGB")
im=ImageOps.fit(im,(240,240),method=Image.Resampling.LANCZOS,centering=(0.5,0.4))
buf=BytesIO()
im.save(buf,format="JPEG",quality=75,optimize=True)
photo=base64.b64encode(buf.getvalue()).decode("ascii")
lines=["BEGIN:VCARD","VERSION:3.0","N:Belhaoud;Hajar;;;","FN:Hajar Belhaoud","ORG:Ejelat Advertising Agency / Track Marketing Solutions","TITLE:Omnichannel Growth Manager","TEL;TYPE=CELL,VOICE:+962788097319","EMAIL;TYPE=INTERNET,WORK:h.belhaoud@track-jo.com","URL:https://www.track-jo.com","NOTE:LinkedIn: https://www.linkedin.com/in/hajarbelhaoud"]
line="PHOTO;ENCODING=b;TYPE=JPEG:"+photo
lines.append(line[:75])
for i in range(75,len(line),74):
    lines.append(" "+line[i:i+74])
lines.append("END:VCARD")
Path("hajar-belhaoud.vcf").write_bytes(("\r\n".join(lines)+"\r\n").encode("utf-8"))
print("Wrote photo-embedded VCF:",len(buf.getvalue()),"JPEG bytes")

# Regenerate photo-embedded contact card on update.

# Alternative vCard 4.0: standards-compliant data URI photo for Apple Contacts testing.
lines4=["BEGIN:VCARD","VERSION:4.0","N:Belhaoud;Hajar;;;","FN:Hajar Belhaoud","ORG:Ejelat Advertising Agency / Track Marketing Solutions","TITLE:Omnichannel Growth Manager","TEL;VALUE=uri;TYPE=cell:tel:+962788097319","EMAIL;TYPE=work:h.belhaoud@track-jo.com","URL:https://www.track-jo.com","NOTE:LinkedIn: https://www.linkedin.com/in/hajarbelhaoud"]
photo4="PHOTO:data:image/jpeg;base64,"+photo
lines4.append(photo4[:75])
for i in range(75,len(photo4),74):
    lines4.append(" "+photo4[i:i+74])
lines4.append("END:VCARD")
Path("hajar-belhaoud-v4.vcf").write_bytes(("\\r\\n".join(lines4)+"\\r\\n").encode("utf-8"))
print("Wrote vCard 4.0 alternate")
