<?php

namespace App\Repositories\Transformers;

class ArticleTransformer extends Transformer {

	public function transform($article) {

		return [
			'title' => $article->title,
			'body' => $article->content,
			'url' => $article->url,
			'thumbnail' => $article->thumbnail,
			'site_name' => $article->site_name,
			'archive_type' => $article->archive_type,
			'slug' => $article->slug,
			'cat_id' => $article->cat_id
		];

	}
}