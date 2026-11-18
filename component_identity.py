"""Canonical IC identity codes, derived from the current taxonomy ID."""
import hashlib


def ic_identity_fields(identifier):
    """Use the same MD5/base36/BIP39 convention as the OOMP framework."""
    from oomp import hex_to_base36
    import oomp_bip39
    digest = hashlib.md5(identifier.encode()).hexdigest()
    fields = {'md5': digest}
    for size in (5, 6, 10):
        fields[f'md5_{size}'] = digest[:size]
        fields[f'md5_{size}_upper'] = digest[:size].upper()
    fields['md5_6_alpha'] = hex_to_base36(digest[:6])
    fields['md5_6_alpha_upper'] = fields['md5_6_alpha'].upper()
    fields.update(oomp_bip39.get_bip39_variants(digest))
    return fields


def refresh_ic_identity(part):
    """Discard any historical seed and use this IC's canonical ID."""
    if part.get('taxonomy_2') == 'ic' and part.get('id'):
        part.pop('identity_seed', None)
        part.update(ic_identity_fields(part['id']))
    return part
