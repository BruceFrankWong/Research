# -*- coding: UTF-8 -*-

__author__ = 'Bruce Frank Wong'


import pytest

from pathlib import Path


@pytest.mark.run(order=5)
def test_database_interface():
    """
    Test for SQLite.
    """
    from InvestmentResearch.utility import PACKAGE_PATH, CONFIGS

    sqlite_path: Path = PACKAGE_PATH.joinpath(CONFIGS['database']['dev']['database'])
    # if sqlite_path.exists():
    #     sqlite_path.unlink()
    
    # assert sqlite_path.exists() is False

    from InvestmentResearch.database import db
    db.connect()
    db.execute_sql('CREATE TABLE test(name varchar);')
    db.commit()
    db.close()

    assert sqlite_path.exists() is True

    sqlite_path.unlink()
    assert sqlite_path.exists() is False


@pytest.mark.run(order=6)
def test_database_initialize_country():
    """
    Test for initialize country.
    """
    from InvestmentResearch.database import db, initialize_country

    db.connect()
    initialize_country()
    db.close()


@pytest.mark.run(order=7)
def test_database_initialize_holiday():
    """
    Test for initialize holiday.
    """
    from InvestmentResearch.database import db, initialize_holiday

    db.connect()
    initialize_holiday()
    db.close()


@pytest.mark.run(order=7)
def test_database_initialize_exchange():
    """
    Test for initialize exchange.
    """
    from InvestmentResearch.database import db, initialize_exchange

    db.connect()
    initialize_exchange()
    db.close()


@pytest.mark.run(order=7)
def test_database_initialize_stock_status():
    """
    Test for initialize stock status.
    """
    from InvestmentResearch.database import db, initialize_stock_status

    db.connect()
    initialize_stock_status()
    db.close()
