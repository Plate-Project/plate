
..

Advanced
=========


Use postman collection json
---------------------------

If use `postman2md <https://github.com/Plate-Project/postman2md>`_ library, easily convert  postman collection json for testing API to markdown. And then you can use converted markdown files as API Documents of Plate. Now must use markdown converting by `postman2md <https://github.com/Plate-Project/postman2md>`_, future we will support postman collection json as the subject of plate. Have any interest of `postman2md <https://github.com/Plate-Project/postman2md>`_, see  `https://github.com/Plate-Project/postman2md <https://github.com/Plate-Project/postman2md>`_ and welcome your contributions at any time, with issues.

.. code-block:: python

    import postman2md
    # create multi markdown file in the directory.
    postman2md.convert(postman_file="example.json.postman_collection")

    # create merged markdown file in the directory.
    postman2md.convert(postman_file="example.json.postman_collection", multi_file=False)


Multi Language Search
---------------------

Multi-language Search is very important part in searching. Plate use `lunr.js <http://lunrjs.com/>`_ for searching contents in API Documents. But `lunr.js <http://lunrjs.com/>`_ has the limit of only english. For available of multi-language search such as Japanese, French,  Plate use `lunr-languages <https://github.com/MihaiValentin/lunr-languages>`_ .

Below is supporting languages :


	* German
	* French
	* Spanish
	* Italian
	* Japanese
	* Dutch
	* Danish
	* Portuguese
	* Finnish
	* Romanian
	* Hungarian
	* Russian
	* Norwegian


