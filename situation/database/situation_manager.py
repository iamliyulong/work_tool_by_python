def tsec_asset_domain_relation_insert(asset_domain_id, asset_ip):
    return f"""
    INSERT INTO situation_manager.tsec_asset_domain_relation
    (asset_domain_id, asset_ip, asset_id)
    VALUES
    ({asset_domain_id}, '{asset_domain_id}.0.0.{asset_ip}',null);
    """
