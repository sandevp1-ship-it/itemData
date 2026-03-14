from dataclasses import dataclass, fields
from fastmcp import FastMCP

mcp = FastMCP(name="Item Data Validator")

# -------- Classes --------

@dataclass
class Item:
    """
    Represents a master item in the product catalog.
    
    Attributes:
        itemID: Unique identifier of the item.
        itemName: Human readable name of the item.
        itemNumber: Business item number used for tracking.
        itemDescription: Description explaining the item usage or details.
        createdDate: Date when the item record was created.
        modifiedDate: Date when the item record was last updated.
    """
    itemID: str
    itemName: str
    itemNumber: str
    itemDescription: str
    createdDate: str
    modifiedDate: str


@dataclass
class TradingPartnerItem:
    """
    Represents item mapping between your system and a trading partner.

    Attributes:
        tradingPartnerID: Unique identifier for the trading partner.
        tradingPartnerName: Name of the trading partner organization.
        itemID: Internal item identifier.
        tradingPartnerItemNumber: Item number used by the trading partner.
        createdDate: Date when the mapping was created.
        modifiedDate: Date when the mapping was last updated.
    """
    tradingPartnerID: str
    tradingPartnerName: str
    itemID: str
    tradingPartnerItemNumber: str
    createdDate: str
    modifiedDate: str


@dataclass
class TradingPartnerRelationship:
    """
    Represents a relationship between two trading partners.

    Attributes:
        relationshipID: Unique identifier for the relationship.
        sourcePartnerID: ID of the source trading partner.
        targetPartnerID: ID of the target trading partner.
        tradingPartnerType: Type of relationship (Supplier, Distributor, Retailer, etc.).
        relationshipStatus: Current status of the relationship (Active/Inactive).
        createdDate: Date when the relationship was created.
        modifiedDate: Date when the relationship was last updated.
    """
    relationshipID: str
    sourcePartnerID: str
    targetPartnerID: str
    tradingPartnerType: str
    relationshipStatus: str
    createdDate: str
    modifiedDate: str


# -------- Modify Methods --------

@mcp.tool(description="Modify the description of an item,  Used for testing item description updates.")
def fetch_item(item: Item) -> Item:
    """
    Updates the item description field.

    Logic:
    - Only the 'itemDescription' field is modified.
    - The value is prefixed with 'modified_'.
    """
    for f in fields(item):
        value = getattr(item, f.name)
        if f.name == "itemDescription":
            setattr(item, f.name, f"modified_{value}")
    return item


@mcp.tool(description="Modify the trading partner item number, Used for testing trading partner item updates.")
def fetch_trading_partner_item(tpi: TradingPartnerItem) -> TradingPartnerItem:
    """
    sharing the trading partner's item number.

    Logic:
    - sending the update tradingpartner Item if any changes
    """
    for f in fields(tpi):
        value = getattr(tpi, f.name)
        if f.name == "tradingPartnerItemNumber":
            setattr(tpi, f.name, f"modified_{value}")
    return tpi


@mcp.tool(description="Toggle the trading partner relationship status between Active and Inactive, used for testing trading partner relationship updates.")
def fetch_trading_partner_relationship(tpr: TradingPartnerRelationship) -> TradingPartnerRelationship:
    """
    fetches the relationship status.

    Logic:
    - checks relationshipStatus is 'Active' or  'Inactive'.
    """
    for f in fields(tpr):
        value = getattr(tpr, f.name)
        if f.name == "relationshipStatus":
            if value == "Active":
                value = "Inactive"
            else:
                value = "Active"
            setattr(tpr, f.name, f"modified_{value}")
    return tpr


# -------- Run MCP Server --------

if __name__ == "__main__":
    mcp.run(transport="http")

     # item = Item(
    #     itemID="101",
    #     itemName="Laptop",
    #     itemNumber="LP1001",
    #     itemDescription="Office Laptop",
    #     createdDate="2026-03-14",
    #     modifiedDate="2026-03-14"
    # )

    # tpi = TradingPartnerItem(
    #     tradingPartnerID="P001",
    #     tradingPartnerName="VendorA",
    #     itemID="101",
    #     tradingPartnerItemNumber="VA-LP1001",
    #     createdDate="2026-03-14",
    #     modifiedDate="2026-03-14"
    # )

    # tpr = TradingPartnerRelationship(
    #     relationshipID="R001",
    #     sourcePartnerID="P001",
    #     targetPartnerID="P002",
    #     tradingPartnerType="Supplier",
    #     relationshipStatus="Active",
    #     createdDate="2026-03-14",
    #     modifiedDate="2026-03-14"
    # )

    # print("Before Modification")
    # print(item)
    # print(tpi)
    # print(tpr)

    # modify_item(item)
    # modify_trading_partner_item(tpi)
    # modify_trading_partner_relationship(tpr)

    # print("\nAfter Modification")
    # print(item)
    # print(tpi)
    # print(tpr)
